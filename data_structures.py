"""Module to learn about Python data structures


Primitive Data Structures

list
    - [1, 2, 3]  SQUARE BRACKETS
    - iterable
    - indexable
    - ordered
    - mutable

tuple
    - (1, 2, 3)  PARENTHESIS
    - iterable
    - indexable
    - ordered
    - immutable

set
    - {1, 2, 3}  CURLY BRACKETS
    - iterable
    - NOT INDEXABLE
    - NOT ORDERED
    - immutable
    - UNIQUE = CANNOT CONTAIN DUPLICATES

dict
    - {"key": "value"}  CURLY BRACKETS
    - iterable
    - NOT INDEXABLE (but you can perform lookups)
    - ordered
    - mutable

"""


def learn_lists():
    """Function to showcase the functionality of a list

    my_list.append(      my_list.count(   my_list.insert(
    my_list.reverse(     my_list.clear(   my_list.extend(
    my_list.pop(         my_list.sort(    my_list.copy(
    my_list.index(       my_list.remove(
    """

    my_list = []  # creating an empty list
    # my_list = list()  # also creates empty list
    my_list = [1, 2, 3, 4, 5]  # starting list

    ## append
    print(my_list)
    my_list.append(2)
    print(my_list)

    ## count
    my_list.append(2)
    print(my_list)
    my_list_count = my_list.count(2)
    print(my_list_count)  # 3

    ## insert
    print(my_list)
    my_list.insert(0, 2)
    print(my_list)

    ## reverse
    print(my_list)
    my_list.reverse()
    print(my_list)

    ## sort
    print(my_list)
    my_list.sort()
    print(my_list)

    ## extend
    print(my_list)
    other_list = [7, 8, 9]
    my_list.extend(other_list)
    print(my_list)  # not to be confused with...
    my_list.append(other_list)
    print(my_list)

    ## pop
    print(my_list)
    last_item_in_list = my_list.pop()
    print(last_item_in_list)
    print(my_list)
    first_item_in_list = my_list.pop(0)
    print(first_item_in_list)
    print(my_list)

    ## copy
    print(my_list)
    my_new_list = my_list.copy()
    print(my_new_list)
    print(id(my_list), id(my_new_list))
    print("The ID is different")

    ## index
    print(my_list)
    position_of_number_five = my_list.index(5)
    print(position_of_number_five)  # 6

    ## remove
    print(my_list)
    my_list.remove(7)
    print(my_list)

    ## clear
    print(my_list)
    my_list.clear()
    print(my_list)


def main():
    """Runs the main process"""

    learn_lists()


if __name__ == "__main__":
    main()
