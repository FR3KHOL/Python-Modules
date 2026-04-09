class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name.capitalize()}: "
              f"{self.height}cm, {self.age} days old")


if __name__ == "__main__":

    plants = [
        Plant("rose", 25, 30),
        Plant("sunflower", 80, 45),
        Plant("cactus", 15, 120)
        ]
    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.show()
