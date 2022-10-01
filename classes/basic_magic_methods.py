"""Module for showcasing magic methods."""


class Number:
    """Represents a Number."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __int__(self):
        return self.value

    def __add__(self, other):
        return int(self) + int(other)

    def __lt__(self, other):
        return int(self) < int(other)

    def __gt__(self, other):
        return int(self) > int(other)

    def __ge__(self, other):
        return int(self) >= int(other)

    def __eq__(self, other):
        return int(self) == int(other)


def main() -> None:
    """Run the main process."""

    x = Number(10)
    y = Number(25)

    # print(x)
    # print(y)

    # print(x + y)
    print(x < y)
    print(x >= y)


if __name__ == "__main__":
    main()
