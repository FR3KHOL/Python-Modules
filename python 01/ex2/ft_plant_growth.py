class Plant:
    def __init__(self, name: str, height: float, lifetime: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.lifetime = lifetime

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.lifetime} days old")

    def age(self) -> None:
        self.lifetime += 1

    def grow(self) -> None:
        self.height += 0.8


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    plant = Plant("Rose", 25.0, 30)
    plant.show()
    initial_height = plant.height

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.grow()
        plant.age()
        plant.show()

    total_growth = plant.height - initial_height
    print(f"Growth this week: {total_growth:.1f}cm")
