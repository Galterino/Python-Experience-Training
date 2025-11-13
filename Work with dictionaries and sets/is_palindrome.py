"""
WRITEN BY GALTERINO
Complex: O(n)

The user enters a string.
I need to write a program that determines whether this string has a permutation that makes it a palindrome.
Then, it should display a corresponding message.

"""

def get_string() -> str:

    """"

    Get user's input string and return it as a string

    """

    return input("Enter a string: ").strip()


def is_string_empty(text:str) -> bool:

    """

    Check if string is empty

    """

    return not text


def histogram(text:str) -> dict:

    """

    Create histogram of given text

    """

    histogram_dict = {}

    for char in text:
        if char not in histogram_dict:
            histogram_dict[char] = 1
        else:
            histogram_dict[char] += 1

    return histogram_dict


def is_palindrome(text:str) -> bool:

    """

    Check if given string is palindrome

    """

    hist = histogram(text)

    values = list(hist.values())
    keys = list(hist.keys())
    singles = values.count(1)
    couple = values.count(2)

    if len(text) <= 2:
        return False
    elif len(text) % 2 == 0:
        count_pairs = len(text) // 2
        if count_pairs == couple:
            return True
    elif len(text) % 2 != 0:
        count_pairs = len(text) // 2
        count_single = len(text) % 2
        if count_single == singles and count_pairs == couple:
            return True
        elif len(keys) == 2 and (hist[keys[0]] > 1 or hist[keys[1]] > 1):
            return True

    return False


user_string = get_string()

if not is_string_empty(user_string):
    if is_palindrome(user_string):
        print("Might be palindrome")
    else:
        print("Not Palindrome")
else:
    print("String is empty")