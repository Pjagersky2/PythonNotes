"""Module for learning Python functions"""


def test_func(positional: int, keyword: int = 2) -> bool:
    """
    This is the test function one line summary

    This is a much more detailed version of the summary for this
    function and it should be multiple lines and very descriptive
    so the user knows exactly how to use it when they go to use
    the function this has many lines

    :param positional: <int> first integer positional argument
    :param keyword: <int> second integer keyword argument

    :rtype: bool
    :return: function always returns true

    """

    print("Running test_func")
    print(f"positional = {positional}")
    print(f"keyword = {keyword}")

    return True


def test_func2(x, y, *numbers, key1="testing", **keyring):
    """Second testing function"""

    print("Running test_func2")
    # print(args[0], args[2])
    # key5 = kwargs.get("key5")
    # if key5:
    #     print(f"Found key5: {key5}")
    # x, y, z = numbers
    # print(x, y, z)
    print(f"x, y = {x}, {y}")
    print(f"key1 = {key1}")
    print(f"numbers = {numbers}")
    print(f"keyring = {keyring}")

    return x, y, numbers, key1, keyring


def main():
    """Runs the main process"""

    # test_func(1)
    # test_func2(1, 2, 3, 4, 5,
    #            key1="something",
    #            key2="password",
    #            key3="secret")
    numbers = 1, 2, 3, 4, 5
    keyring = {
        "key1": "something",
        "key2": "password",
        "key3": "secret"
    }
    # results = test_func2(*numbers, **keyring)
    # print(f"results = {results}")
    # x, y, nums, key1, keys = results
    x, y, nums, key1, keys = test_func2(*numbers, **keyring)
    print(x, y, nums, key1, keys)
    # test_func2(1, 2, 3, 4, 5,
    #            key1="something",
    #            key2="password",
    #            key3="secret")


if __name__ == "__main__":
    main()
