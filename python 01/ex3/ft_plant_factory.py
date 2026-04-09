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
    print("=== Plant Factory Output ===")
    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120),
    ]
    for plant in plants:
        print("Created: ", end="")
        plant.show()
