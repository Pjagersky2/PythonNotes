"""Module for showcasing magic methods with iterables."""
from basic_classes import Human


class Parent(Human):
    """Represents a Parent."""

    def __init__(self, name, age, children):
        super().__init__(name, age)
        self.children = children

    def __str__(self):
        return f"{self.name.title()} has children {str(self.children)}"

    def __len__(self):
        return len(self.children)

    def __iter__(self):
        for child in self.children:
            yield child


def main() -> None:
    """Run the main process."""

    peter_children = [1, 2, 3]
    frank_children = [9, 8, 7]

    peter = Parent("peter", 50, peter_children)
    frank = Parent("frank", 55, frank_children)

    # print(sum(peter))
    # print(sum(frank))

    # for x, y in zip(peter, frank):
    #     print(x, y)

    print(peter)
    for child in peter:
        print(child)

    print(frank)
    for child in frank:
        print(child)

    peter.greet()
    frank.greet()


if __name__ == "__main__":
    main()
