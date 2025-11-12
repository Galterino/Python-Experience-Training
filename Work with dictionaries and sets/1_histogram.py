""" CREATED BY GALTERINO """
def histogram() -> dict:

    """
    Create a histogram.

    :return: histogram_dictionary
    """

    user_text = input("Enter the user text: ")

    histogram_dict = dict()

    for symbol in user_text:
        if symbol in histogram_dict:
            histogram_dict[symbol] += 1
        else:
            histogram_dict[symbol] = 1

    return histogram_dict


def print_histogram(histogram_dict:dict):

    """

    Display histogram with formatted output.

    :param histogram_dict: Dictionary to display

    """

    for symbol, count in sorted(histogram_dict.items()):
        print(f"{symbol}: {count}")


def invert_histogram(histogram_dict:dict) -> dict:

    """
    func makes histogram inverted, where numbers are keys, and symbols are values

    :param histogram_dict:
    :return inverted_histogram_dict:
    """

    inverted_dict = dict()

    for symbol, count in histogram_dict.items():
        if count in inverted_dict:
            inverted_dict[count].append(symbol)
        else:
            inverted_dict[count] = [symbol]

    return inverted_dict


histogram = histogram()
print_histogram(histogram)
inverted_histogram = invert_histogram(histogram)
print_histogram(inverted_histogram)