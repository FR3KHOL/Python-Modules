from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission_rules(self) -> 'SpaceMission':
        if not self.mission_id.startswith('M'):
            raise ValueError("Mission ID must start with 'M'")

        has_leadership = any(
            c.rank in (Rank.COMMANDER, Rank.CAPTAIN) for c in self.crew
        )
        if not has_leadership:
            msg = "Mission must have at least one Commander or Captain"
            raise ValueError(msg)

        if not all(c.is_active for c in self.crew):
            raise ValueError("All crew members must be active")

        if self.duration_days > 365:
            exp = sum(1 for c in self.crew if c.years_experience >= 5)
            if exp / len(self.crew) < 0.5:
                raise ValueError("Long missions need 50% experienced crew")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    c1 = CrewMember(member_id="C01", name="Sarah Connor",
                    rank=Rank.COMMANDER, age=45,
                    specialization="Mission Command", years_experience=20)
    c2 = CrewMember(member_id="C02", name="John Smith",
                    rank=Rank.LIEUTENANT, age=35,
                    specialization="Navigation", years_experience=10)
    c3 = CrewMember(member_id="C03", name="Alice Johnson",
                    rank=Rank.OFFICER, age=28,
                    specialization="Engineering", years_experience=4)

    try:
        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.fromisoformat("2025-01-01T00:00:00"),
            duration_days=900,
            crew=[c1, c2, c3],
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print(f"Mission: {valid_mission.mission_name}")
        print(f"ID: {valid_mission.mission_id}")
        print(f"Destination: {valid_mission.destination}")
        print(f"Duration: {valid_mission.duration_days} days")
        print(f"Budget: ${valid_mission.budget_millions}M")
        print(f"Crew size: {len(valid_mission.crew)}")
        print("Crew members:")
        for c in valid_mission.crew:
            print(f"- {c.name} ({c.rank.value}) - {c.specialization}")
        print("=========================================")
    except ValidationError as e:
        print(e)

    try:
        SpaceMission(
            mission_id="M2025_MOON",
            mission_name="Lunar Outpost",
            destination="Moon",
            launch_date=datetime.fromisoformat("2025-06-01T00:00:00"),
            duration_days=30,
            crew=[c2, c3],
            budget_millions=500.0
        )
    except ValidationError as e:
        print("Expected validation error:")
        for err in e.errors():
            msg = err.get('msg', '').replace('Value error, ', '')
            print(msg)


if __name__ == "__main__":
    main()
