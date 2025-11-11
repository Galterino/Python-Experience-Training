""" WROTE BY GALTERINO """

def get_strings_list():

    """

    Create a few strings

    :return String_1, String_2:

    """

    return input("Main string: ").strip(), input("Second string: ").strip()

def check_space_in_string(string:str) -> bool:

    """

    Check if a string contains space

    :param string:
    :return Boolean:

    """

    return not ' ' in string

def if_string_empty(string) -> bool:

    """

    check if a string is empty

    :return boolean:
    :param string:

    """

    return not string

def check_shift(main:str, second:str):

    """

    Check if a string can be shifted and return shift if that exists

    :param main:
    :param second:
    :return shift:

    """

    main_length = len(main)
    second_length = len(second)
    main_symbol_target = main[0]
    shift = 0

    list_symbols_second = list(second)


    is_target_in_second = False

    if main_length != second_length:
        return "error_length"
    elif main == second:
        return 'error_equal'
    elif main_symbol_target in second:
        is_target_in_second = True

    if is_target_in_second:
        for i in range(main_length):
            if "".join(list_symbols_second) != main:
                last_symbol = list_symbols_second.pop()
                list_symbols_second.insert(0, last_symbol)
                shift += 1
            else:
                return shift

    return 0

main_string, second_string = get_strings_list()
is_spaces = check_space_in_string(main_string) and check_space_in_string(second_string)
is_empty = if_string_empty(main_string) or if_string_empty(second_string)

if not is_empty and is_spaces:
    shift_value = check_shift(main_string, second_string)
    if shift_value == 0:
        print("The first row cannot be obtained from the second row using a cyclic shift.")
    elif shift_value == 'error_one_symbol':
        print("There are no one symbols in lines")
    elif shift_value == "error_length":
        print("These strings don't have the same length.")
    elif shift_value == "error_equal":
        print("The main string is equal to the second string.")
    else:
        print(f"The first row is obtained from the second row by shifting it {shift_value} positions.")
else:
    print("There is a space in lines or line is empty.")