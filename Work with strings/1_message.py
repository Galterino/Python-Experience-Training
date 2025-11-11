""" MADE BY GALTERINO """

PUNCTUATION_MARKS = {".", ",", ":", "...", "?", "-", "'", "(", ")", ";", "!"}

def get_punctuation_marks():
    """

    There are punctuation marks list returned

    """

    return PUNCTUATION_MARKS

def not_empty_message(message:str) -> bool:
    """

    Checks if the message is empty or not

    """

    if message:
        return True
    else:
        return False

def get_message():
    return input("Enter your message: ").strip()

def punctuation_mark_check_position(word:str):

    """

    the function checks the first occurrence of a punctuation mark in a word

    :param word: string
    :return: index before first occurrence of punctuation mark
    :return: list of punctuation marks in the end of word

    """

    index = 0
    punctuation_marks_end_list = []

    for symbol in word:
        if symbol not in get_punctuation_marks():
            index += 1
        else:
            punctuation_marks_end_list.append(symbol)

    punctuation_marks_str = "".join(punctuation_marks_end_list)

    return index, punctuation_marks_str

def reverse_message_step_words(message:str) -> str:

    """
    The user enters a text consisting of words and punctuation marks.
    The program reverses (writes in reverse order) all the words in the text,
    leaving the punctuation marks unchanged.
    A word in the text is defined as a sequence of uppercase and lowercase Cyrillic letters.

    :param: str message
    :return: str reversed_message

    """

    if not_empty_message(message):

        words = message.split()

        for i in range(len(words)):
            if words[i][-1] not in get_punctuation_marks():
                words[i] = words[i][::-1]
            elif words[i][-1] in get_punctuation_marks():
                index_position, end_part = punctuation_mark_check_position(words[i])
                words[i] = words[i][:index_position][::-1]
                words[i] = "".join((words[i], end_part))
            else:
                continue
        else:
            new_message = " ".join(words)
            return new_message
    else:
        print("Error: Message is empty.")
        return message


user_message = get_message()
print(f"New message: {reverse_message_step_words(user_message)}")
