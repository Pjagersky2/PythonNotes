"""Module describing Python primitive data types"""
import math

"""
Primitive Data Types:

- Data types that make up Python at the core

Boolean     (bool)      [True or False]
Integer     (int)       [-5, 10, 0, 1, 100]
Decimal     (float)     [3.14, -0.5, 0.0]
String      (str)       ["hello", 'world', '13', "0.5"]
Imaginary   (complex)   [5j+1]

"""


def boolean_usage():
    """Example usage for boolean data types"""

    x = True
    print(x)
    # print(f"{x=}")
    print(type(x))

    y = False
    print(y)
    # print(f"{y=}")
    print(type(y))

    print(x and y)  # False
    print(x or y)  # True

    print(int(x))  # 1
    print(int(y))  # 0

    x_int = int(x)
    x_float = float(x)
    x_str = str(x)
    print(x_int, x_float, x_str)


def integer_usage():
    """Example usage for integer data types"""

    x = 15
    y = 3

    print(x)
    print(y)

    print(type(x))
    print(type(y))

    print(x + y)  # 18
    print(x - y)  # 12
    print(x * y)  # 45
    print(x / y)  # 5.0

    #round(value, decimal_places)
    value = 11 / 3
    print(round(value, 3))
    print(math.ceil(value))
    print(math.floor(value))
    print(11 // 3)  # 3.6666666667

    print(bool(10))  # True
    print(bool(-10))  # True
    print(bool(0))  # False


def decimal_usage():
    """Example usage for decimal data types"""

    x = 3.14
    print(x)
    print(type(x))

    print(int(x))  # 3

    y = 9.99
    print(int(y))  # 9


def string_usage():
    """Example usage for decimal data types"""

    x = "Hello"
    print(x)
    print(type(x))

    y = "World"
    print(x + y)  # HelloWorld
    # print(x - y)  # not allowed
    # print(x * y)  # not allowed (str * str)
    print(x * 5)  # HelloHelloHelloHelloHello
    # print(x / 5)  # not allowed

    print("10" + "15")

    print(bool(x))  # True
    # print(int(x))
    # print(float(x))
    print(int("10") + 15)  # 25
    print(float("3.14") + 5)  # 8.14

    print(bool(""))  # False


def main():
    """Runs the main function"""

    print("Boolan examples...")
    boolean_usage()

    print("\nInteger examples...")
    integer_usage()

    print("\nDecimal examples...")
    decimal_usage()

    print("\nInteger examples...")
    string_usage()


if __name__ == "__main__":
    main()
