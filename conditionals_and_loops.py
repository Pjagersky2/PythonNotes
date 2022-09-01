"""Module for explaining conditionals and loops in Python"""


def conditionals(condition=(20 < 20.1)):
    """Function to showcase Python conditional statements"""

    if condition:
        print("Fail")
    else:
        print("Pass")

    return "Pass" if not condition else "Fail"


def loops(max_num):
    """Function to showcase Python loop statements"""

    # squares = []
    # for number in range(max_num):
    #     square = number ** 2
    #     squares.append(square)

    # return squares

    return [char * 2 for char in "hello"]


def main():
    """Runs the main process"""

    result = conditionals(5001 > (4001 + 1000))
    print(result)
    result = loops(8)
    print(result)


if __name__ == "__main__":
    main()
