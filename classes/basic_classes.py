"""Module for showcasing classes and objects."""


class Human:
    """Represents a Human."""

    def __init__(self, name: str, age: int) -> None:
        """Initialize a Human object."""

        self.name = name
        self.age = age

    def __bool__(self) -> bool:
        """Boolean representation of a Human type object."""

        return True if self.age > 25 else False

    def greet(self) -> None:
        """Introduce yourself."""

        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


def main() -> None:
    """Run the main process."""

    peter = Human("peter", 24)
    adam = Human("adam", 27)

    peter.greet()
    adam.greet()

    print(bool(peter))
    print(bool(adam))


if __name__ == "__main__":
    main()
