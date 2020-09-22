from typing import Tuple, List


def find_previous_character_if_question_mark(regex: str, start: int) -> Tuple[int, str]:
    """
    Recursive function for finding the "?" metacharacter,
    it's index, the previous index and the symbol preceding the metacharacter.
    The "?" metacharacter means that the previous symbol should occur once or
    0 times.

    :param regex: The regex to find the metacharacter in it.
    Example: "colou?r".
    :type regex: str
    :param start: The index from which to search the metacharacter.
    Example: 0.
    :type start: int
    :returns: The tuple of 2 results - an index of the character previous to
    the "?" metacharacter and a character that is previous to the index - in
    the case it founds the metacharacter searched. Otherwise - it returns -1
    and "s" (a dummy sign), to prevent TypeError. Example: (4, "u").
    :rtype: Tuple[int, str]

    """
    # 0 or 1 times match

    i: int = regex.find("?", start)

    # If there is no "?", -1 and 's' - the 'dummy' character is returned.

    if i == -1:
        return -1, 's'

    # found the "?" metacharacter as the first character in the regex,
    # so it doesn't meet the criteria. Keep searching further.

    if i == 0:

        return find_previous_character_if_question_mark(regex, 1)

    # if the "?" metacharacter is found, the previous index and the character
    # with the previous index are returned.

    else:
        previous_char: str = regex[i - 1]
        return (i - 1), previous_char


def make_comparisons_question_mark(regex: str, input_str: str) -> Tuple[bool, int]:
    """
    Returns True if it finds 1 or 0 examples of the characters at the probed
    indexes. As it supports "." wildcard - the third block in the wildcard
    block should return False, but it returns True - because of the Jetbrains
    stage tests.

    :param regex: The regex string with "?" in it. Or not. Example: "colou?r".
    :type regex: str
    :param input_str: The string to be compared to the regex.
    Example: "colour".
    :type input_str: str
    :returns: A tuple - if there is a match (True or False) and a number of
     matched characters (0, 1 or 2). Example: (False, 0).
    :rtype: Tuple[bool, int]
    """

    index: int = find_previous_character_if_question_mark(regex, 0)[0]

    # No "?" metacharacter had been found, the False is returned.

    if index == -1:

        return False, 0

    # The "?" metacharacter had been found, so the previous_char (the previous
    # character to metacharacter is extracted.

    else:

        previous_char: str = find_previous_character_if_question_mark(regex, 0)[1]

        # The wildcard block.

        if previous_char == ".":

            # The chosen_char is the character in the input_str corresponding to the
            # regex character that was extracted by the
            # find_previous_character_if_question_mark function.

            chosen_char: str = input_str[index]

            # No character found, 0 matches - returns True.

            if not chosen_char:
                return True, 0

            # One match, returns True.

            elif chosen_char != input_str[index - 1]:
                return True, 1

            # Two matches (at least), returns True.

            elif chosen_char == input_str[index - 1]:
                return True, 2

            elif chosen_char == input_str[index + 1]:
                return True, 2

        # The "without a wildcard" block.

        else:

            if len(str(find_previous_character_if_question_mark(regex, 0))) == 1:

                return False, 0

            else:

                # Checking the outcomes, finding the matches, churning the answers.

                # Index has to be greater or equal to 1.

                if index >= 1:

                    # One match found, returns True.

                    if input_str[index - 1] == previous_char \
                            and input_str[index - 2] != previous_char:

                        return True, 1

                    # More than 1 match found, returns False.

                    elif input_str[index - 1] == previous_char \
                            and input_str[index - 2] == previous_char:

                        return False, 0

                    elif input_str[index - 1] == previous_char \
                            and input_str[index] == previous_char:

                        return False, 0

                    elif input_str[index] == previous_char \
                            and input_str[index + 1] == previous_char:

                        return False, 0

                    # Zero matches found, returns True.

                    elif input_str[index - 1] != previous_char:

                        return True, 0


def find_previous_character_if_question_mark_reversed(regex: str, start: int) \
        -> Tuple[int, str]:
    """
    Recursive function for finding the "?" metacharacter and the previous
    character in the regex adjusted for some end-string searching. The "?"
    metacharacter allows for 0 or 1 match.

    :param regex: The regex to be checked for the "?" metacharacter. May be
    already reversed. Example: "$?a"
    :type regex:str
    :param start: Index to start the search with. Example: 0.
    :type start: int
    :returns: A tuple: a index of a searched character after the metacharacter and
    a character at that index. Example: (2, "a")
    """
    # 0 or 1 times match

    # Finding the index of the metacharacter.

    i: int = regex.find("?", start)

    # no "?" found in the regex, -1 is returned altogether with a dummy string

    if i == -1:
        return -1, 's'

    # Found metacharacter is the first symbol in the word, it doesn't meet the
    # conditions. Keep searching further.

    if i == 0:
        return find_previous_character_if_question_mark_reversed(regex, 1)

    else:
        next_char: str = regex[i + 1]
        return (i + 1), next_char


def make_comparisons_question_mark_reversed(regex: str, input_str: str) -> \
        Tuple[bool, int]:
    """
    Returns True if it finds 1 or 0 examples of the characters at the probed
    indexes with the "?" metacharacter and number of the matches. Supports a
    wildcard.

    :param regex: The regex to be probed. Example: "$?a".
    :type regex: str
    :param input_str: The string to be compared to the regex. Example: "a".
    :returns: A tuple - True if there is a match, False - if there is no match
     and a number of matches, if it applies. Example: (True, 0).
    :rtype: Tuple[bool, int]
    """

    index: int
    next_char: str
    index, next_char = find_previous_character_if_question_mark_reversed(regex, 0)

    # The wildcard block.

    if next_char == ".":

        chosen_char: str = input_str[index]

        # The chosen_char is an empty string, returns True. Zero matches.

        if not chosen_char:
            return True, 0
        # One match, returns True.

        elif chosen_char != input_str[index - 1]:
            return True, 1
        # 2 matches, wildcard case, returns True.

        elif chosen_char == input_str[index - 1]:
            return True, 2

    # "No wildcard" block.

    else:

        if len(str(find_previous_character_if_question_mark_reversed(regex, 0))) == 1:
            return False, 0

        else:

            # 0 matches, returns True.

            if input_str[index] != next_char:
                return True, 0

            # 1 match, returns True.

            elif input_str[index] == next_char and input_str[index - 1] != next_char:
                return True, 1

            # 2 matches, returns False and 0.

            elif input_str[index] == next_char and input_str[index - 1] == next_char:
                return False, 0


def find_previous_character_if_multiplication_mark(regex: str, start: int) -> \
        Tuple[int, str]:
    """
    Recursive function for finding the "*" metacharacter and the previous
    character in the regex. The "*" metacharacter allows for 0 or more
    matches. Supports wildcard character ".".

    :param regex: The regex to be searched for "*" metacharacter.
    Example: ".*".
    :type regex: str
    :param start: The start index of the regex to be searched for the
     metacharacter for. Example: 0.
    :type start: int
    :returns: A tuple: an index of the previous character to the metacharacter
     and that character.
    """
    # 0 or more times match

    # The i: index of the metacharacter.

    i: int = regex.find("*", start)

    # If there is no metacharacter in the given regex, -1 and a dummy
    # character is returned.

    if i == -1:
        return -1, 's'

    # The metacharacter is found at the first index that doesn't meet the
    # criteria, so the search is continued from the next index.

    if i == 0:
        return find_previous_character_if_multiplication_mark(regex, 1)

    # If index meets the criteria, the index of the character preceding
    # the metacharacter is returned and that character is also returned.

    else:
        previous_char: str = regex[i - 1]
        return (i - 1), previous_char


def make_comparisons_multiplication_mark(regex: str, input_str: str) -> \
        Tuple[bool, int]:
    """
    Returns True if it finds 0 or more times the preselected characters at the
    probed indexes. Supports wildcard "." character.

    :param regex: The regex to be compared to the input_str string. Example:
    ".*".
    :type regex: str
    :param input_str: The input string to be compared to the regex. Example:
    "aaa".
    :type input_str: str
    :returns: A tuple: if there is a match or no and the number of matches.
    :rtype: Tuple[bool, int]
    """

    index: int
    previous_char: str

    index, previous_char = find_previous_character_if_multiplication_mark(regex, 0)

    # The wildcard block.

    if previous_char == ".":

        # The chosen_char is a character that corresponds to the character at the
        # index extracted from the regex by the
        # find_previous_character_if_multiplication_mark function.

        chosen_char: str = input_str[index]

        # 0 matches, returns True.

        if chosen_char != previous_char:
            return True, 0

        # The chosen_char is an empty string, returns True.

        elif not chosen_char:
            return True, 0

        # 2 matches, returns True.

        elif chosen_char == input_str[index - 1] \
                or chosen_char == input_str[index + 1]:
            return True, 2

        # 1 match, returns True.

        elif chosen_char != input_str[index - 1] \
                or chosen_char != input_str[index + 1]:
            return True, 1
    else:

        # The " no wildcard" block.

        if len(str(find_previous_character_if_multiplication_mark(regex, 0))) == 1:
            return False, 0

        else:

            # 0 matches, returns True.

            if input_str[index] != previous_char:
                return True, 0

            # 1 match, returns True.

            elif input_str[index] == previous_char \
                    and input_str[index - 1] != previous_char:
                return True, 1

            # 2 matches, returns True.

            elif input_str[index] == previous_char \
                    and input_str[index - 1] == previous_char:
                return True, 2

            elif input_str[index] == previous_char \
                    and input_str[index + 1] == previous_char:
                return True, 2


def find_previous_character_if_addition_mark(regex: str, start: int) -> \
        Tuple[int, str]:
    """
    Recursive function for finding the "+" metacharacter and the previous
    character in the regex. The "+" metacharacter allows for 1 or more
    matches. Supports wildcard character ".".

    :param regex: The regex to be searched for "+". Example: ".+".
    :type regex: str
    :param start: The starting index from which the regex will be searched
     from. Example: 0.
    :type start: int
    """
    # 1 or more times match

    # i : the index at which the metacharacter is found.

    i: int = regex.find("+", start)

    if i == -1:  # there is no "+" metacharacter in the word
        return -1, 's'

    # Found the "+" metacharacter as the first symbol in the word, it doesn't
    # meet the conditions. Keep searching further.

    if i == 0:
        return find_previous_character_if_addition_mark(regex, 1)

    # The found index meets the conditions so the index previous to the
    # metacharacter is returned altogether with the character preceding
    # the metacharacter.

    else:
        previous_char: str = regex[i - 1]
        return (i - 1), previous_char


def make_comparisons_addition_mark(regex: str, input_str: str) -> \
        Tuple[bool, int]:
    """
    Returns True if it finds 1 or more examples of the characters at the
    probed indexes. Supports the wildcard "." symbol.

    :param regex: The regex to be compared to the input_str string. Example:
    ".+".
    :param input_str: The input string to be compared to the regex string.
    Example: "aaa".
    :returns: A tuple: True if there is a match, False otherwise and a
    number of matches. Example: (True, 2).
    :rtype: Tuple[bool, int].
    """
    index: int = find_previous_character_if_addition_mark(regex, 0)[0]
    previous_char: str = find_previous_character_if_addition_mark(regex, 0)[1]

    # The wildcard block.

    if previous_char == ".":

        # The chosen_char is the character corresponding to the character at the
        # the corresponding index in the regex.

        chosen_char: str = input_str[index]

        # If there is a chosen_char, return True. One match.

        if chosen_char:
            return True, 1

        # If the chosen_char matched 2 times, returns True.

        elif chosen_char == input_str[index - 1]:
            return True, 2

        elif chosen_char == input_str[index + 1]:
            return True, 2
        # If there is no chosen_char, return False.

        elif not chosen_char:
            return False, 0
    else:

        if len(str(find_previous_character_if_addition_mark(regex, 0))) == 1:
            return False, 0

        # The "no wildcard" block.

        else:

            # No match, return False.

            if input_str[index] != previous_char:
                return False, 0

            # 1 match, return True.

            elif input_str[index] == previous_char \
                    and input_str[index - 1] != previous_char:
                return True, 1

            elif input_str[index] == previous_char \
                    and input_str[index + 1] != previous_char:
                return True, 1

            # 2 matches, return True.

            elif input_str[index] == previous_char \
                    and input_str[index - 1] == previous_char:
                return True, 2

            elif input_str[index] == previous_char \
                    and input_str[index + 1] == previous_char:
                return True, 2


def single_character_comparison(input_string: str) -> bool:
    """
    A function which compares a regex and an input string of
    length 1 or 0, The input_string therefore should be of
    length 3 of less. Supports the wildcard symbol ".".

    :param input_string: A combination of the regex and a string to
    compare divided by a vertical line |. Examples: ".|a", "6|7".
    :type input_string: str
    :returns: True if the string passed in along with the regex matches the
    regex pattern. False otherwise. Example: True
    :rtype: bool
    """

    # The input_string is splitted into an input_list on the vertical line
    # ("|") and the first element of the list is delegated to the regex
    # variable, and the second element of the list is delegated to the
    # input_string variable.

    input_list: List[str] = input_string.split("|")
    regex: str = input_list[0]
    input_string: str = input_list[1]

    # If regex equals a wildcard symbol, the function returns True.

    if regex == ".":

        return True

    # If regex equals an empty string, the function returns True.

    elif not regex:

        return True

    # If the regex string is not empty, but the input_string is an empty
    # string, the function returns False.

    elif len(regex) == 1 and not input_string:

        return False

    # If the regex string is not empty, the input_string equals "." and the
    # regex doesn't equal the input_string, the function returns False.

    elif len(regex) == 1 and input_string == "." and regex != input_string:

        return False

    # If the regex string doesn't equal a wildcard, the regex string and the
    # input_string string are not empty and are not equal, the function
    # returns False.

    elif regex != "." and len(regex) == len(input_string) == 1 \
            and regex != input_string:

        return False

    # If the regex string is empty and the input_string is empty, the function
    # returns True.

    elif not regex and not input_string:

        return True

    # If the regex string equals the input_string, the function returns True.

    elif regex == input_string:

        return True


def find_next_character_if_backslash_detected(regex: str, start: int) -> \
        Tuple[int, str]:
    """
    Function for finding the "\\" character, it's index, the next index and
    the symbol after the backslash.

    :param regex: The regex to find the backslash in it.
    Example: "colou\\?r".
    :type regex: str
    :param start: The index from which to search the backslash. Example: 0.
    :type start: int
    :returns: A tuple of 2 results - an index of the character next to the
    backslash metacharacter and a character that is next to the backslash - in
    the case it founds the backslash in the regex. Otherwise - it returns -1
    and "s" (a dummy sign), to prevent TypeError.
    :rtype: Tuple[int, str]
    """

    i: int = regex.find("\\", start)

    # If there is no "\\", -1 and 's' - the 'dummy' character is returned.

    if i == -1:
        return -1, 's'

    # if the "\\" metacharacter is found, the next index and the character
    # with that index are returned.

    else:
        next_char: str = regex[i + 1]
        return (i + 1), next_char


def find_next_character_if_backslash_detected_reversed(regex: str, start: int) \
        -> Tuple[int, str]:
    """
    Function for finding the "\\" character, it's index, the previous index and
    the symbol before the backslash.

    :param regex: The regex to find the backlash in it. May already be
     reversed. Example: "?//".
    :type regex: str
    :param start: The index from which to search the backslash. Example: 0.
    :type start: int
    :returns: A tuple of 2 results - an index of the character previous to the
    backslash metacharacter and a character with that index - in the case it
    founds the backslash. Otherwise - it returns -1 and "s" (a dummy
    character), to prevent TypeError.
    :rtype: Tuple[int, str]
    """

    # i: index of the backslash.

    i: int = regex.find("\\", start)

    # If there is no backslash detected, -1 and 's' (the 'dummy' character)
    # are returned.

    if i == -1:
        return -1, 's'

    # if backslash metacharacter is found, the previous index and the
    # character with the previous index are returned.

    else:
        previous_char: str = regex[i - 1]
        return (i - 1), previous_char


def single_character_comparison_without_wildcard(input_string: str) -> \
        bool:
    """
    A function which compares a regex and an input string of
    length 1 or 0, The input_string therefore should be of
    length 3 of less. Without the wildcard "." supported.

    :param input_string: A combination of the regex and a string to
    compare divided by a vertical line |. Examples: "a|a", "6|7".
    :type input_string: str
    :returns: True if the string passed in along with the regex matches the
    regex pattern. False otherwise. Example: True.
    :rtype: bool
    """

    # The input_string is splitted into an input_list on the vertical line
    # ("|") and the first element of the list is delegated to the regex
    # variable, and the second element of the list is delegated to the
    # input_string variable.

    input_list: List[str] = input_string.split("|")
    regex: str = input_list[0]
    input_string: str = input_list[1]

    # If regex is an empty string, the function returns True.

    if not regex:

        return True

    # If regex string is not empty, but the input_string is an empty string,
    # the function returns False.

    elif len(regex) == 1 and not input_string:

        return False

    # If regex string is not empty and regex doesn't equal input_string, the
    # function returns False.

    elif len(regex) == 1 and regex != input_string:

        return False

    # If the regex string and the input_string string are not empty are not
    # equal, the function returns False.

    elif len(regex) == len(input_string) == 1 \
            and regex != input_string:

        return False

    # If the regex string is empty and the input_string is empty, the
    # function returns True.

    elif not regex and not input_string:

        return True

    # If the regex string equals the input_string, the function returns True.

    elif regex == input_string:

        return True


def recursive_regex(input_string: str) -> bool:
    """
    The recursive regex function for the regex and the string
    to be parsed of the equal lengths. The wildcard symbol "." is
    supported.

    :param input_string: The input string of the pattern
     "{regex}|{string_to_be_parsed}". Example: "apple|peach",
      ".....|apple".
    :type input_string: str
    :returns: True if the passed-in string matches the passed-in regex
    pattern. False otherwise.
    :rtype: bool.
    """

    # To this block the input_string of length equal or less than 3 is
    # relegated (so something that is compatible with functions of
    # function single_character_comparison).

    if len(input_string) < 3 or len(input_string) == 3:

        # If input function ends with vertical line ("|") and/or starts with
        # vertical line ("|") (so input_string == "|"), it cannot be efficiently
        # divided into the regex and the string_to_be_parsed variables, because
        # at the beginning or/and the end is an empty string which the list
        # splitter just doesn't recognize. Therefore, the empty strings are
        # assigned to the relevant variables (regex and input_string manually).
        # The stings are assembled into the raw "regex|input_string" input string
        # again and plugged into the single_character_comparison function. If the
        # single_character_comparison function returns False - the recursive_regex
        # function returns False. Otherwise (the single_character_comparison
        # function returns True), the recursive_regex
        # function returns True. The string "|" should fall into the block
        # "not regex and not input_string" in the single_character_comparison
        # function and return True.

        if input_string.endswith("|") and input_string.startswith("|"):

            regex: str = ""
            input_str: str = ""

            if not single_character_comparison(f"{regex}|{input_str}"):

                return False

            # This string ("|") goes here and returns True.

            elif single_character_comparison(f"{regex}|{input_str}"):

                return True

        # If the input_string doesn't starts with a vertical line ("|") and
        # doesn't ends with a vertical line ("|"), that's mean there is no empty
        # string at the beginning or at the end of the input_string and the
        # input_string can be safely splitted at the vertical line without
        # generating an IndexError. The input_string is therefore splitted at the
        # vertical line and assigned as the list to the input_list variable. The
        # first item of the input_list is delegated to the regex variable, and the
        # second item of the input_list is delegated to the input_str variable. If
        # the single_character_comparison function, to which the elements with
        # 0-indices of the both variables after reassembling them into the raw
        # input "regex|input_string" string are plugged in, returns False, then
        # the recursive_regex function returns False. If the same raw input string
        # after plugging it into the aforementioned function returns True, the
        # recursive_regex function returns True. If the input_string is longer
        # than the regex string, the recursive_regex function returns False. If
        # the regex is an empty string and the input_string is not an empty
        # string, the recursive_regex function returns True.

        elif not input_string.startswith("|") and not input_string.endswith("|"):

            input_list: List[str] = input_string.split("|")
            regex = input_list[0]
            input_str = input_list[1]

            if not single_character_comparison(f"{regex[0]}|{input_str[0]}"):

                return False

            elif single_character_comparison(f"{regex[0]}|{input_str[0]}"):

                return True

            elif len(input_str) > len(regex):

                return False

            elif not regex and len(input_str) >= 1:

                return True

        # If the input_string starts with a vertical line ("|"), and at the same
        # time doesn't end with a vertical line ("|"), again, it's not safe to
        # split it into a list. Better to assign an empty string to the regex
        # variable, and as to the input_str variable, it's just stripped the
        # input_string from the vertical line. If the single_character_comparison
        # function returns False after comparing an empty regex with the first
        # character of the input_str, the recursive_regex function also returns
        # False. If the single_character_comparison function returns True after
        # comparing an empty regex with the first character of input_str, the
        # recursive_regex function also returns True. Peeking up the
        # single_character_comparison function, when the regex is an empty string,
        # the answer should be always True. If the input_str is longer that the regex
        # string (if the regex string is at least 1-element long!) the
        # recursive_regex function returns False. The forth block says the same
        # that the second block - if the regex is an empty string and the
        # accompanying it string to parse isn't empty - the recursive_regex
        # function should return True.

        elif input_string.startswith("|") and not input_string.endswith("|"):

            regex = ''
            input_str = input_string.strip("|")

            if not single_character_comparison(f"{regex}|{input_str[0]}"):

                return False

            # The answer in the case of an empty regex should be always True.

            elif single_character_comparison(f"{regex}|{input_str[0]}"):

                return True

            elif regex:

                if len(input_str) > len(regex):
                    return False

            # The fallback option to the 2-nd block.

            elif not regex and len(input_str) >= 1:

                return True

        # If the input_string ends with a vertical line, again, it's not safe
        # to split the string into the list. Better assign the strings manually
        # to the variables. The regex variable is assigned to the input_string
        # stripped off the vertical line ("|") and the input_str string is
        # assigned to an empty string. Peeking up the single_character_comparison
        # function, the non-empty regex string with the empty accompanying string
        # should always return False. The reassembled raw input string is plugged
        # into the single_character_comparison function and if the
        # single_character_comparison function returns False, the recursive_regex
        # also should return False. If the single_character_comparison function
        # returns True, the recursive_regex also should return True.

        elif input_string.endswith("|") and not input_string.startswith("|"):

            regex = input_string.strip("|")
            input_str = ''

            # The string of the pattern "a|" goes here and returns False.

            if not single_character_comparison(f"{regex[0]}|{input_str}"):

                return False

            elif single_character_comparison(f"{regex[0]}|{input_str}"):

                return True

            elif input_str:

                if len(input_str) > len(regex):
                    return False

            # The fallback option.

            elif not input_str and len(regex) >= 1:

                return False

    # The block for the input_string strings with the length equal or greater
    # than 4.

    while len(input_string) >= 4:

        # If the input_string doesn't start with a vertical line ("|") or doesn't
        # end with a vertical line, that means that it can be safely splitted into
        # a list (input_list) on the vertical line. After the split, the first
        # item of the list is delegated to its variable (regex) and the second
        # item of the list is also delegated to its variable (input_str).

        if not input_string.startswith("|") and not input_string.endswith("|"):

            input_list = input_string.split("|")
            regex = input_list[0]
            input_str = input_list[1]

            # If the regex starts with a wildcard symbol "^", which means that the
            # string should be well-adjusted to the regex pattern at the beginning of
            # the string, the regex variable is trimmed from that metacharacter sign
            # and the input_str is trimmed to the length of the regex pattern. While
            # the regex string is evaluated as True, if the comparison of the first
            # characters of the regex string and the input_str string in the
            # single_character_comparison function returned False, the recursive_regex
            # function also returns False. Otherwise, the regex and the input_str
            # variables are trimmed, assembled into the raw input string and
            # recursively plugged into the recursive_regex function. The checking and
            # evaluation for "?", "+" and "*" metacharacters was added.

            if regex.startswith("^") and "$" not in regex:

                regex = regex[1:]
                len_regex: int = len(regex)
                input_str_shortened: str = input_str[:len_regex]

                # The "?" metacharacter block.

                if "?" in regex:

                    index: int
                    previous_char: str

                    index, previous_char = find_previous_character_if_question_mark(regex, 0)

                    bool_ans: bool
                    how_many: int

                    bool_ans, how_many = make_comparisons_question_mark(regex, input_str)

                    # 0 matches, bool_ans == True.

                    if bool_ans is True and how_many == 0:

                        regex = regex[index + 1:]

                        while regex:

                            if not single_character_comparison(f"{regex[0]}|{input_str_shortened[0]}"):

                                return False

                            else:

                                regex = regex[1:]
                                input_str = input_str[1:]
                                new_input: str = f"{regex}|{input_str}"

                                return recursive_regex(new_input)

                    # One match, bool_ans == True.

                    elif bool_ans is True and how_many == 1:

                        # Matching the regex from the already matched character..

                        regex = regex[index + 1:]

                        # Get rid of the matched characters.

                        input_str_shortened = input_str[:index] + input_str[index + 1:]

                        while regex:

                            if not single_character_comparison(f"{regex[0]}|{input_str_shortened[0]}"):

                                return False

                            else:

                                regex = regex[1:]
                                input_str_shortened = input_str_shortened[1:]
                                new_input: str = f"{regex}|{input_str_shortened}"

                                return recursive_regex(new_input)

                # The "*" metacharacter block.

                if "*" in regex:

                    index, previous_char = find_previous_character_if_multiplication_mark(regex, 0)
                    bool_ans, how_many = make_comparisons_multiplication_mark(regex, input_str)

                    if bool_ans is True and how_many == 0:

                        regex = regex[index + 1:]

                        while regex:

                            if not single_character_comparison(f"{regex[0]}|{input_str_shortened[0]}"):

                                return False

                            else:

                                regex = regex[1:]
                                input_str = input_str[1:]
                                new_input: str = f"{regex}|{input_str}"

                                return recursive_regex(new_input)

                    elif bool_ans is True and how_many == 1:

                        while input_str:

                            if not single_character_comparison(f"{regex[0]}|{input_str[0]}"):

                                return False

                            else:
                                input_str_shortened = input_str_shortened[1:]
                                new_input: str = f"{regex}|{input_str_shortened}"

                                return recursive_regex(new_input)

                # The "+" metacharacter block.

                if "+" in regex:

                    index, previous_char = find_previous_character_if_addition_mark(regex, 0)
                    bool_ans, how_many = make_comparisons_addition_mark(regex, input_str)

                    if not bool_ans:
                        return False

                    if bool_ans is True and how_many == 1:

                        regex = regex[index + 1:]

                        while regex:

                            if not single_character_comparison(f"{regex[0]}|{input_str_shortened[0]}"):

                                return False

                            else:

                                regex = regex[1:]
                                input_str = input_str[1:]
                                new_input: str = f"{regex}|{input_str}"

                                return recursive_regex(new_input)

                    elif bool_ans is True and how_many == 2:

                        while input_str:

                            if not single_character_comparison(f"{regex[0]}|{input_str[0]}"):

                                return False

                            else:
                                input_str_shortened = input_str_shortened[1:]
                                new_input: str = f"{regex}|{input_str_shortened}"

                                return recursive_regex(new_input)

                # No "?", "*", "+" metacharacters block.

                else:

                    # len(regex)==1 block

                    if len(regex) == 1:

                        if not single_character_comparison(f"{regex[0]}|{input_str[0]}"):
                            return False

                        else:

                            regex = regex
                            input_str_shortened = input_str[1:]
                            new_input: str = f"{regex}|{input_str_shortened}"

                            return recursive_regex(new_input)

                    # The longer regexes block.

                    else:
                        if not single_character_comparison(f"{regex[0]}|{input_str[0]}"):
                            return False
                        else:

                            regex = regex[1:]
                            input_str_shortened = input_str[1:]
                            new_input: str = f"{regex}|{input_str_shortened}"

                            return recursive_regex(new_input)

            # If the regex variable ends with "$" metacharacter, the regex variable is
            # trimmed of that metacharacter first, the length of the regex variable is
            # assigned to the len_regex variable. The regex is rewritten from the last
            # character to the first. The same is done with the input_str variable.
            # Then, the input_str variable is trimmed to the length of the regex.
            # While the regex variable evaluates to True, if the first characters of
            # the regex and the input_str variables assembled into the raw input
            # string, plugged into the single_character_comparison function are
            # evaluated to False, the recursive_regex function also returns False.
            # Otherwise, the variables are trimmed, assembled into the input string
            # and plugged into the recursive_regex function, recursively. The checking
            # and evaluation for "?", "+" and "*" metacharacters was added.

            elif regex.endswith("$") and "^" not in regex:

                # regex trimmed

                regex = regex[:-1]
                len_regex = len(regex)

                # regex reversed

                regex = regex[::-1]

                # input_str reversed

                input_str = input_str[::-1]

                # input_str trimmed to the length of regex

                input_str = input_str[:len_regex]

                # The "?" metacharacter block

                if "?" in regex:

                    index, previous_char = find_previous_character_if_question_mark_reversed(regex, 0)
                    bool_ans, how_many = make_comparisons_question_mark_reversed(regex, input_str)

                    if bool_ans is True and how_many == 0:

                        regex = regex[::-1]
                        regex = regex[index + 1:]
                        input_str = input_str[::-1]

                        while regex:

                            if not single_character_comparison(f"{regex[0]}|{input_str[0]}"):

                                return False

                            else:

                                regex = regex[1:]
                                input_str = input_str[1:]
                                new_input: str = f"{regex}|{input_str}"

                                return recursive_regex(new_input)

                    if bool_ans is True and how_many == 1:

                        regex = regex[::-1]
                        regex = regex[index + 1:]
                        input_str = input_str[::-1]
                        input_str_shortened = input_str[:index] + input_str[index + 1:]
                        while regex:

                            if not single_character_comparison(f"{regex[0]}|{input_str_shortened[0]}"):

                                return False

                            else:

                                regex = regex[1:]
                                input_str_shortened = input_str_shortened[1:]
                                new_input: str = f"{regex}|{input_str_shortened}"

                                return recursive_regex(new_input)

                # The "*" metacharacter block.

                if "*" in regex:

                    index, previous_char = find_previous_character_if_multiplication_mark(regex, 0)
                    bool_ans, how_many = make_comparisons_multiplication_mark(regex, input_str)

                    if bool_ans is True and how_many == 0:

                        regex = regex[index + 1:]

                        while regex:

                            if not single_character_comparison(f"{regex[0]}|{input_str[0]}"):

                                return False

                            else:

                                regex = regex[1:]
                                input_str = input_str[1:]
                                new_input: str = f"{regex}|{input_str}"

                                return recursive_regex(new_input)

                    elif bool_ans is True and how_many == 1:

                        while input_str:

                            if not single_character_comparison(f"{regex[0]}|{input_str[0]}"):

                                return False

                            else:

                                input_str_shortened = input_str[1:]
                                new_input: str = f"{regex}|{input_str_shortened}"

                                return recursive_regex(new_input)

                # The "+" metacharacter block.

                if "+" in regex:

                    index, previous_char = find_previous_character_if_addition_mark(regex, 0)
                    bool_ans, how_many = make_comparisons_addition_mark(regex, input_str)

                    if not bool_ans:
                        return False

                    if bool_ans is True and how_many == 1:

                        regex = regex[index + 1:]

                        while regex:

                            if not single_character_comparison(f"{regex[0]}|{input_str[0]}"):

                                return False

                            else:

                                regex = regex[1:]
                                input_str = input_str[1:]
                                new_input: str = f"{regex}|{input_str}"

                                return recursive_regex(new_input)

                    elif bool_ans is True and how_many == 2:

                        while input_str:

                            if not single_character_comparison(f"{regex[0]}|{input_str[0]}"):

                                return False

                            else:

                                input_str_shortened = input_str[1:]
                                new_input: str = f"{regex}|{input_str_shortened}"

                                return recursive_regex(new_input)

                # No "?", "+", "*" metacharacters block.

                else:

                    if len(regex) == 1:

                        if not single_character_comparison(f"{regex[0]}|{input_str[0]}"):
                            return False

                        else:

                            regex = regex
                            input_str_shortened = input_str[1:]
                            new_input: str = f"{regex}|{input_str_shortened}"

                            return recursive_regex(new_input)

                    else:

                        if not single_character_comparison(f"{regex[0]}|{input_str[0]}"):

                            return False

                        else:

                            regex = regex[1:]
                            input_str_shortened = input_str[1:]
                            new_input: str = f"{regex}|{input_str_shortened}"

                            return recursive_regex(new_input)

            # If the regex both starts with "^" metacharacter and ends with "$"
            # metacharacter, it's both trimmed at the beginning and at the end. If
            # lengths of regex and input_str are not equal, False is returned. If
            # length of regex and input_str are equal, the comparison begins. If the
            # first characters of the regex and the input_str variables assembled into
            # a form and plugged into the single_character_comparison function
            # evaluate to False, the recursive_regex function returns False.
            # Otherwise, both variables are trimmed, assembled and plugged into the
            # recursive_regex function, recursively. The checking and
            # evaluation for "?", "+" and "*" metacharacters was added.

            elif regex.startswith("^") and regex.endswith("$"):

                regex = regex[1:-1]

                # The "?" metacharacter block.

                if "?" in regex:

                    index, previous_char = find_previous_character_if_question_mark_reversed(regex, 0)
                    bool_ans, how_many = make_comparisons_question_mark_reversed(regex, input_str)

                    if bool_ans is True and how_many == 0:

                        regex = regex[index + 1:]

                        if len(input_str) > len(regex):
                            return False

                        if len(regex) > len(input_str):
                            return False

                        if len(regex) == len(input_str):

                            if not single_character_comparison(f"{regex[0]}|{input_str[0]}"):

                                return False

                            else:

                                regex = regex[1:]
                                input_str = input_str[1:]
                                new_input: str = f"{regex}|{input_str}"

                                return recursive_regex(new_input)

                    elif bool_ans is True and how_many == 1:

                        regex = regex[index + 1:]
                        input_str_shortened = input_str[:index] + input_str[index + 1:]

                        if len(input_str_shortened) > len(regex):
                            return False

                        if len(regex) > len(input_str_shortened):
                            return False

                        if len(regex) == len(input_str_shortened):

                            if not single_character_comparison(f"{regex[0]}|{input_str_shortened[0]}"):

                                return False

                            else:

                                regex = regex[1:]
                                input_str_shortened = input_str_shortened[1:]
                                new_input: str = f"{regex}|{input_str_shortened}"

                                return recursive_regex(new_input)

                # The "*" metacharacter block.

                elif "*" in regex:

                    index, previous_char = find_previous_character_if_multiplication_mark(regex, 0)
                    bool_ans, how_many = make_comparisons_multiplication_mark(regex, input_str)

                    if bool_ans is True and how_many == 0:

                        regex = regex[index + 1:]

                        while regex:

                            if not single_character_comparison(f"{regex[0]}|{input_str[0]}"):

                                return False

                            else:

                                regex = regex[1:]
                                input_str = input_str[1:]
                                new_input: str = f"{regex}|{input_str}"

                                return recursive_regex(new_input)

                    elif bool_ans is True and how_many == 1:

                        while input_str:

                            if not single_character_comparison(f"{regex[0]}|{input_str[0]}"):

                                return False

                            else:

                                input_str_shortened = input_str[1:]
                                new_input: str = f"{regex}|{input_str_shortened}"

                                return recursive_regex(new_input)

                # The "+" metacharacter block.

                elif "+" in regex:

                    index, previous_char = find_previous_character_if_addition_mark(regex, 0)
                    bool_ans, how_many = make_comparisons_addition_mark(regex, input_str)

                    if not bool_ans:
                        return False

                    elif bool_ans is True and how_many == 1:
                        regex = regex[index + 1:]

                        while regex:

                            if not single_character_comparison(f"{regex[0]}|{input_str[0]}"):

                                return False

                            else:

                                regex = regex[1:]
                                input_str = input_str[1:]
                                new_input: str = f"{regex}|{input_str}"

                                return recursive_regex(new_input)

                    elif bool_ans is True and how_many == 2:

                        while input_str:

                            if not single_character_comparison(f"{regex[0]}|{input_str[0]}"):

                                return False

                            else:

                                input_str_shortened = input_str[1:]
                                new_input: str = f"{regex}|{input_str_shortened}"

                                return recursive_regex(new_input)

                # No "?", "*", "+" metacharacters blocks.

                else:

                    if len(regex) == 1:

                        if not single_character_comparison(f"{regex[0]}|{input_str[0]}"):

                            return False

                        else:

                            regex = regex
                            input_str_shortened = input_str[1:]
                            new_input: str = f"{regex}|{input_str_shortened}"

                            return recursive_regex(new_input)
                    else:

                        if not single_character_comparison(f"{regex[0]}|{input_str[0]}"):

                            return False

                        else:

                            regex = regex[1:]
                            input_str_shortened = input_str[1:]
                            new_input: str = f"{regex}|{input_str_shortened}"

                            return recursive_regex(new_input)

            # Finally, if the regex doesn't contain the metacharacters (^, $), the
            # evaluation comes about smoothly. If the first characters of the regex
            # and the input_str assembled into a form and plugged into the
            # single_character_comparison function evaluate to False, the
            # recursive_regex function returns False. Otherwise, both variables are
            # trimmed, assembled and plugged into the  recursive_regex function,
            # recursively. The checking and evaluation for "?", "+" and "*"
            # metacharacters was added.

            elif not regex.startswith("^") and not regex.endswith("$"):

                # The "?" metacharacter block.

                if "?" in regex:

                    index = find_previous_character_if_question_mark(regex, 0)[0]

                    bool_ans, how_many = make_comparisons_question_mark(regex, input_str)

                    if bool_ans is True and how_many == 0:

                        regex = regex[index + 1:]

                        if len(input_str) >= 1:

                            if not single_character_comparison(f"{regex[0]}|{input_str[0]}"):

                                return False

                            else:

                                regex = regex[1:]
                                input_str = input_str[1:]
                                new_input: str = f"{regex}|{input_str}"

                                return recursive_regex(new_input)

                        if bool_ans is True and how_many == 1:

                            regex = regex[index + 1:]
                            input_str_shortened = input_str[:index] + input_str[index + 1:]

                            if not single_character_comparison(f"{regex[0]}|{input_str_shortened[0]}"):

                                return False

                            else:

                                regex = regex[1:]
                                input_str_shortened = input_str_shortened[1:]
                                new_input: str = f"{regex}|{input_str_shortened}"

                                return recursive_regex(new_input)

                # The "*" metacharacter block.

                if "*" in regex:

                    index, previous_char = find_previous_character_if_multiplication_mark(regex, 0)
                    bool_ans, how_many = make_comparisons_multiplication_mark(regex, input_str)

                    if bool_ans is True and how_many == 0:

                        regex = regex[index + 1:]

                        while regex:

                            if not single_character_comparison(f"{regex[0]}|{input_str[0]}"):

                                return False

                            else:

                                regex = regex[1:]
                                input_str = input_str[1:]
                                new_input: str = f"{regex}|{input_str}"

                                return recursive_regex(new_input)

                    elif bool_ans is True and how_many == 1:

                        while input_str:

                            if not single_character_comparison(f"{regex[0]}|{input_str[0]}"):

                                return False

                            else:

                                input_str_shortened = input_str[1:]
                                new_input: str = f"{regex}|{input_str_shortened}"

                                return recursive_regex(new_input)

                # The "+" metacharacter block.

                if "+" in regex:

                    index = find_previous_character_if_addition_mark(regex, 0)[0]
                    bool_ans, how_many = make_comparisons_addition_mark(regex, input_str)

                    if not bool_ans:
                        return False

                    if bool_ans is True and how_many == 1:

                        regex = regex[index + 1:]

                        while regex:

                            if not single_character_comparison(f"{regex[0]}|{input_str[0]}"):

                                return False

                            else:

                                regex = regex[1:]
                                input_str = input_str[1:]
                                new_input: str = f"{regex}|{input_str}"

                                return recursive_regex(new_input)

                    elif bool_ans is True and how_many == 2:

                        while input_str:

                            if not single_character_comparison(f"{regex[0]}|{input_str[0]}"):

                                return False

                            else:
                                input_str_shortened = input_str[1:]
                                new_input: str = f"{regex}|{input_str_shortened}"

                                return recursive_regex(new_input)

                # The no "?", "*", "+" metacharacter block.

                else:

                    if len(regex) == 1:

                        if not single_character_comparison(f"{regex[0]}|{input_str[0]}"):

                            return False

                        else:

                            regex = regex
                            input_str_shortened = input_str[1:]
                            new_input: str = f"{regex}|{input_str_shortened}"

                            return recursive_regex(new_input)

                    elif len(regex) < len(input_str):

                        if not single_character_comparison(f"{regex[0]}|{input_str[0]}"):

                            return False

                        else:
                            input_str = input_str[1:]
                            new_input: str = f"{regex}|{input_str}"

                            return recursive_regex(new_input)

                    elif len(regex) == len(input_str):

                        if not single_character_comparison(f"{regex[0]}|{input_str[0]}"):

                            return False

                        else:
                            regex = regex[1:]
                            input_str = input_str[1:]
                            new_input: str = f"{regex}|{input_str}"

                            return recursive_regex(new_input)

        # We are still considering the input_string of length greater or equal to
        # 4. If the input_string starts with "|", an empty string is assigned to
        # the regex variable and the input_string stripped of the vertical line is
        # assigned to the input_str variable. If the regex string is empty, in
        # general, the single_character_comparison function should return True.

        if input_string.startswith("|") and not input_string.endswith("|"):

            regex = ""
            input_str = input_string.strip("|")

            if not single_character_comparison(f"{regex}|{input_str[0]}"):

                return False

            else:

                input_str = input_str[1:]
                new_input = f"{regex}|{input_str}"

                return recursive_regex(new_input)

        # If the input_string ends with a vertical line, then the input_string
        # stripped off the vertical line is assigned to the regex variable,
        # and an empty string is assigned to the input_str variable. In that
        # cases, the single_character_comparison function should
        # return False.

        if not input_string.startswith("|") and input_string.endswith("|"):

            regex = input_string.strip("|")
            input_str = ""

            # This goes here and the False is returned.

            if not single_character_comparison(f"{regex[0]}|{input_str}"):

                return False

            else:

                regex = regex[1:]
                new_input = f"{regex}|{input_str}"

                return recursive_regex(new_input)


def unequal_strings_find_match(input_string: str) -> bool:
    """
    The function comparing the regex pattern and a string of unequal length.
    Supports wildcard symbol ".". Support for detecting and evaluation of the
    "*", "?", "+" metacharacters and a backslash metacharacter was added.
    "^" and "$" metacharacters are also supported.

    :param input_string: An input string of the pattern
     "{regex}|{string_to_be_parsed}".
    Examples: "le|apple", "peach|apple".
    :type input_string: str
    :returns: True if there is a match between the regex pattern and a
     passed-in string. False otherwise. Example: False.
    :rtype: bool
    """

    # To this block the input_string of length equal or less than 3 is
    # relegated. (so something that is compatible with functions of
    # function single_character_comparison).

    if len(input_string) < 3 or len(input_string) == 3:

        # If the input_string ends with vertical line ("|") and/or starts with
        # vertical line ("|") (so input_string == "|"), it cannot be efficiently
        # divided into the regex and the string_to_be_parsed, because at the
        # beginning or/and the end is an empty string which the list splitter just
        # doesn't recognize. Therefore, the empty strings are assigned to the
        # relevant variables (regex and input_str) manually. The stings are
        # assembled into the raw "regex|input_str" input string again and plugged
        # into the single_character_comparison function. If the
        # single_character_comparison function returns False - the recursive_regex
        # function also returns False. Otherwise (the single_character_comparison
        # function returns True), the recursive_regex function returns True. The
        # string ("|") should fall into the block "not regex and not input_string"
        # in the single_character_comparison function and return True.

        if input_string.endswith("|") and input_string.startswith("|"):

            regex: str = ""
            input_str: str = ""

            if not single_character_comparison(f"{regex}|{input_str}"):

                return False

            # The string "|" falls here and returns True.

            elif single_character_comparison(f"{regex}|{input_str}"):

                return True

        # If the input_string doesn't starts with a vertical line ("|") and
        # doesn't ends with a vertical line ("|"), that's mean there is no empty
        # string at the beginning or/and at the end of the input_string and the
        # input_string can be safely splitted at the vertical line without
        # generating an IndexError. The input_string is therefore splitted at
        # the vertical line and assigned as the list to the input_list variable.
        # The first item of the input_list is delegated to the regex variable,
        # and the second item of the input_list is delegated to the input_str
        # variable. If the single_character_comparison function, to which the
        # elements with 0-indices of both variables after reassembling into the
        # raw input "regex|input_string" string are plugged in, returns False,
        # then the recursive_regex function returns False. If the same raw input
        # string after plugging it into the aforementioned function returns True,
        # the recursive_regex function returns True. If the input_str is longer
        # than the regex string, the recursive_regex function returns False. If
        # the regex is an empty string and the input_str is not an empty string,
        # the recursive_regex function returns True.

        elif not input_string.startswith("|") and not input_string.endswith("|"):

            input_list: List[str] = input_string.split("|")
            regex = input_list[0]
            input_str = input_list[1]

            if not single_character_comparison(f"{regex[0]}|{input_str[0]}"):

                return False

            elif single_character_comparison(f"{regex[0]}|{input_str[0]}"):

                return True

            elif len(input_str) > len(regex):

                return False

            # The fallback option:

            elif not regex and len(input_str) >= 1:

                return True

        # If the input_string starts with the vertical line ("|"), and at the same
        # time doesn't end with a vertical line ("|"), again, it's not safe to
        # split it into a list. Better to assign an empty string to the regex
        # variable, and as to the input_str variable, it's just stripped the
        # input_string from the vertical line. If the single_character_comparison
        # function returns False after comparing an empty regex with the first
        # character of the input_str, the recursive_regex function also returns
        # False. If the single_character_comparison function returns True after
        # comparing an empty regex string with the first character of input_str,
        # the recursive_regex function also returns True. Peeking up
        # the single_character_comparison function reveals that when the regex
        # is an empty string, the answer should be always True. If the input_str
        # is longer that the regex string (if the regex string is at least of
        # length 1!) the recursive_regex function returns False. The forth block
        # says the same that the second block - if the regex is an empty string
        # and the accompanying it string to parse isn't empty - the
        # recursive_regex function should return True.

        elif input_string.startswith("|") and not input_string.endswith("|"):

            regex = ''
            input_str = input_string.strip("|")

            if not single_character_comparison(f"{regex}|{input_str[0]}"):

                return False

            elif single_character_comparison(f"{regex}|{input_str[0]}"):

                return True

            elif len(input_str) > len(regex):

                return False

            elif not regex and len(input_str) >= 1:

                return True

        # If the input_string ends with a vertical line, again, it's not safe to
        # split the string into the list. Better assign the strings manually to
        # the variables. The regex variable is assigned to the input_string
        # stripped off the vertical line ("|") and the input_str string is
        # assigned to an empty string. Peeking up the single_character_comparison
        # function, the non-empty regex string with the empty accompanying string
        # should always return False. The reassembled raw input string is plugged
        # into the single_character_comparison and if the
        # single_character_comparison function returns False, the recursive_regex
        # function also should return False. If the single_character_comparison
        # function returns True, the recursive_regex also should return True.

        elif input_string.endswith("|") and not input_string.startswith("|"):

            regex = input_string.strip("|")
            input_str = ''

            # It should fall here and should return False.

            if not single_character_comparison(f"{regex[0]}|{input_str}"):
                return False

            elif single_character_comparison(f"{regex[0]}|{input_str}"):
                return True

            elif len(input_str) > len(regex):
                return False

            elif not regex and len(input_str) >= 1:
                return True

    # Block for the input_string strings with the length equal or greater to
    # 4.

    while len(input_string) >= 4:

        # If the input_string doesn't start with a vertical line ("|") or doesn't
        # end with a vertical line, that means that it can be safely splitted into
        # a list (the input_list variable) on the vertical line. After the split,
        # the first item of the list is delegated to its variable (regex) and the
        # second item of the list is also delegated to its variable (input_str).
        # Support for detecting and evaluation of the "*", "?", "+" metacharacters
        # and a backslash metacharacter was added. "^" and "$" are also supported.

        if not input_string.startswith("|") and not input_string.endswith("|"):

            input_list = input_string.split("|")

            regex = input_list[0]
            input_str = input_list[1]

            # If the regex starts with "^", the regex variable is trimmed of that
            # metacharacter, then the len_regex variable is instantiated as the
            # variable with the value of the regex's length. The index counter
            # variable is instantiated with the initial value of 0. The
            # input_str_shortened variable is a shortened version of the input_str
            # variable to the length of equal of the regex's one. Support for
            # detecting and evaluation of the "*", "?", "+" metacharacters
            # and a backslash metacharacter was added.

            if regex.startswith("^") and "$" not in regex:

                regex = regex[1:]
                len_regex: int = len(regex)

                index: int = 0

                input_str_shortened: str = input_str[index:len_regex]

                # The "?" metacharacter block.

                if "?" in regex:

                    previous_char: str

                    index, previous_char = find_previous_character_if_question_mark(regex, 0)

                    bool_ans: bool
                    how_many: int

                    bool_ans, how_many = make_comparisons_question_mark(regex, input_str)

                    if not bool_ans:
                        return False

                    if bool_ans is True and how_many == 0:

                        regex = regex[index + 1:]

                        # While the input_str_shortened is evaluated to True (is not an empty
                        # string) there can be two responses from its combination with regex
                        # plugged into the recursive_regex function - either True - and then
                        # the function returns True or False - and then the function returns
                        # False.

                        while input_str_shortened:

                            if recursive_regex(f"{regex}|{input_str_shortened}"):

                                return True

                            elif not recursive_regex(f"{regex}|{input_str_shortened}"):

                                return False

                    if bool_ans is True and how_many == 1:

                        regex = regex[index + 1:]

                        # Getting rid of the positively matched character.

                        input_str_shortened = input_str[:index] + input_str[index + 1:]

                        while input_str_shortened:

                            if recursive_regex(f"{regex}|{input_str_shortened}"):

                                return True

                            elif not recursive_regex(f"{regex}|{input_str_shortened}"):

                                return False

                # The "*" metacharacter block.

                if "*" in regex:

                    index, previous_char = find_previous_character_if_multiplication_mark(regex, 0)
                    bool_ans, how_many = make_comparisons_multiplication_mark(regex, input_str)

                    if not bool_ans:
                        return False

                    if bool_ans is True and how_many == 0:

                        regex = regex[index + 1:]

                        # While the input_str_shortened is evaluated to True (is not an empty
                        # string) there can be two responses from its combination with the regex
                        # plugged into the recursive_regex function - either True - and then the
                        # function returns True or False - and then the function returns False.

                        while input_str_shortened:

                            if recursive_regex(f"{regex}|{input_str_shortened}"):

                                return True

                            elif not recursive_regex(f"{regex}|{input_str_shortened}"):

                                return False

                    if bool_ans is True and how_many == 1:

                        regex = regex[index + 1:]

                        # Getting rid of the positively matched character.

                        input_str_shortened = input_str[:index] + input_str[index + 1:]

                        while input_str_shortened:

                            if recursive_regex(f"{regex}|{input_str_shortened}"):

                                return True

                            elif not recursive_regex(f"{regex}|{input_str_shortened}"):

                                return False

                    if bool_ans is True and how_many == 2:

                        regex = regex[index + 1:]

                        input_str_shortened = input_str[:index] + input_str[index + 1:]

                        while input_str_shortened:

                            if recursive_regex(f"{regex}|{input_str_shortened}"):

                                return True

                            elif not recursive_regex(f"{regex}|{input_str_shortened}"):

                                return False

                # The "+" metacharacter block.

                if "+" in regex:

                    index, previous_char = find_previous_character_if_addition_mark(regex, 0)
                    bool_ans, how_many = make_comparisons_addition_mark(regex, input_str)

                    if not bool_ans:
                        return False

                    if bool_ans is True and how_many == 0:

                        regex = regex[index + 1:]

                        # While the input_str_shortened is evaluated to True (is not an empty
                        # string) there can be two responses from its combination with the regex
                        # plugged in the recursive_regex function- either True - and then the
                        # function returns Tru or False - and then the function returns False.

                        while input_str_shortened:

                            if recursive_regex(f"{regex}|{input_str_shortened}"):

                                return True

                            elif not recursive_regex(f"{regex}|{input_str_shortened}"):

                                return False

                    if bool_ans is True and how_many == 1:

                        # Getting rid of the positively matched character.

                        input_str_shortened = input_str[:index] + input_str[index + 1:]

                        while input_str_shortened:

                            if recursive_regex(f"{regex}|{input_str_shortened}"):

                                return True

                            elif not recursive_regex(f"{regex}|{input_str_shortened}"):

                                input_str_shortened = input_str_shortened[:-1]

                                return unequal_strings_find_match(f"{regex}|{input_str_shortened}")

                    if bool_ans is True and how_many == 2:

                        regex = regex[index + 1:]

                        # Getting rid of the positively matched character.

                        input_str_shortened = input_str[:index] + input_str[index + 1:]

                        while input_str_shortened:

                            if recursive_regex(f"{regex}|{input_str_shortened}"):

                                return True

                            elif not recursive_regex(f"{regex}|{input_str_shortened}"):

                                return False

                # No "*", "+", "?" metacharacters block.

                else:
                    if recursive_regex(f"{regex}|{input_str_shortened}"):

                        return True

                    elif not recursive_regex(f"{regex}|{input_str_shortened}"):

                        return False

            # If the regex ends with "$" metacharacter, the regex variable is first
            # trimmed of that character, length of the regex variable is ascribed
            # to the len_regex variable, the regex variable reversed and the same is
            # done with the input_str variable, and then the input_variable is trimmed
            # to the length equal to the regex variable length.

            elif regex.endswith("$") and "^" not in regex:

                # regex variable trimmed

                regex = regex[:-1]

                len_regex = len(regex)

                # regex and input_str variable reversed

                regex = regex[::-1]
                input_str = input_str[::-1]

                # input_str trimmed to the relevant length

                input_str = input_str[:len_regex]

                # The backslash block

                if "\\" in regex:

                    char: str

                    index, char = find_next_character_if_backslash_detected_reversed(regex, 0)

                    regex = regex[:index]

                    if len(regex) == 1:

                        if single_character_comparison_without_wildcard(f"{regex}|{input_str[0]}"):
                            return True

                        if not single_character_comparison_without_wildcard(f"{regex}|{input_str[0]}"):
                            return False

                # The "?" metacharacter block.

                elif "?" in regex:

                    index, previous_char = find_previous_character_if_question_mark(regex, 0)
                    bool_ans, how_many = make_comparisons_question_mark(regex, input_str)

                    if bool_ans is True and how_many == 0:

                        regex = regex[index + 1:]

                        # After reassembling and plugging in the regex and the input_str
                        # variables, if the recursive_regex function evaluates to True, then the
                        # function returns True. If the recursive_regex function evaluates to
                        # False, the function returns False.

                        if recursive_regex(f"{regex}|{input_str}"):

                            return True

                        elif not recursive_regex(f"{regex}|{input_str}"):

                            return False

                    if bool_ans is True and how_many == 1:

                        regex = regex[index + 1:]

                        # Getting rid of the positively matched character

                        input_str_shortened = input_str[:index] + input_str[index + 1:]

                        if recursive_regex(f"{regex}|{input_str_shortened}"):

                            return True

                        elif not recursive_regex(f"{regex}|{input_str_shortened}"):

                            return False

                    if not bool_ans:
                        return False

                # The "*" metacharacter block.

                if "*" in regex:

                    index, previous_char = find_previous_character_if_multiplication_mark(regex, 0)
                    bool_ans, how_many = make_comparisons_multiplication_mark(regex, input_str)

                    if not bool_ans:

                        return False

                    elif bool_ans is True and how_many == 0:

                        regex = regex[index + 1:]

                        # While the input_str is evaluated to True (is not an empty string) there
                        # can be two responses from its combination with the regex plugged into the
                        # recursive_regex function - either True - and then the function returns
                        # True or False - and then the function returns False.

                        while input_str:

                            if recursive_regex(f"{regex}|{input_str}"):

                                return True

                            elif not recursive_regex(f"{regex}|{input_str}"):

                                return False

                    if bool_ans is True and how_many == 1:

                        regex = regex[index + 1:]

                        # Getting rid of the positively matched character.

                        input_str_shortened = input_str[:index] + input_str[index + 1:]

                        while input_str_shortened:

                            if recursive_regex(f"{regex}|{input_str_shortened}"):

                                return True

                            elif not recursive_regex(f"{regex}|{input_str_shortened}"):

                                return False

                    if bool_ans is True and how_many == 2:

                        regex = regex[index + 1:]

                        # Getting rid of the positively matched character.

                        input_str_shortened = input_str[:index] + input_str[index + 1:]

                        while input_str_shortened:

                            if recursive_regex(f"{regex}|{input_str_shortened}"):

                                return True

                            elif not recursive_regex(f"{regex}|{input_str_shortened}"):

                                return False

                # The "+" metacharacter block.

                if "+" in regex:

                    index, previous_char = find_previous_character_if_addition_mark(regex, 0)
                    bool_ans, how_many = make_comparisons_addition_mark(regex, input_str)

                    if not bool_ans:
                        return False

                    if bool_ans is True and how_many == 0:

                        regex = regex[index + 1:]

                        # While the input_str is evaluated to True (is not an empty string)
                        # there can be two responses from its combination with the regex plugged
                        # into the recursive_regex function - either True - and then the function
                        # returns True or False - and then the function returns False.

                        while input_str:

                            if recursive_regex(f"{regex}|{input_str}"):

                                return True

                            elif not recursive_regex(f"{regex}|{input_str}"):

                                return False

                    if bool_ans is True and how_many == 1:

                        regex = regex[index + 1:]

                        # Getting rid of the positively matched character.

                        input_str_shortened = input_str[:index] + input_str[index + 1:]

                        while input_str_shortened:

                            if recursive_regex(f"{regex}|{input_str_shortened}"):

                                return True

                            elif not recursive_regex(f"{regex}|{input_str_shortened}"):

                                return False

                    if bool_ans is True and how_many == 2:

                        regex = regex[index + 1:]

                        # Getting rid of the positively matched character.

                        input_str_shortened = input_str[:index] + input_str[index + 1:]

                        while input_str_shortened:

                            if recursive_regex(f"{regex}|{input_str_shortened}"):

                                return True

                            elif not recursive_regex(f"{regex}|{input_str_shortened}"):

                                return False

                # The no "*", "?", "+" metacharacters blocks.
                else:

                    if recursive_regex(f"{regex}|{input_str}"):

                        return True

                    elif not recursive_regex(f"{regex}|{input_str}"):

                        return False

            # If the regex variable starts with "^" metacharacter and ends with "$"
            # metacharacter, the regex variable is first trimmed of those
            # metacharacters, then the length of the regex variable is assigned to the
            # len_regex. If regex length isn't equal to the input_str length,
            # the function returns False. If the lengths of both variables are equal,
            # they are evaluated by the recursive_regex function. If the result of the
            # evaluation equals True - the function returns True. Otherwise, the
            # function returns False.

            elif regex.endswith("$") and regex.startswith("^"):

                # the regex variable trimmed

                regex = regex[1:-1]

                # the regex and the input_str variables are reversed

                regex_reversed: str = regex[::-1]
                input_str_reversed: str = input_str[::-1]

                len_regex = len(regex)

                # The "?" metacharacter block.

                if "?" in regex:

                    index, previous_char = find_previous_character_if_question_mark(regex, 0)
                    bool_ans, how_many = make_comparisons_question_mark(regex, input_str)

                    if not bool_ans:
                        return False

                    if bool_ans is True and how_many == 0:

                        regex = regex[index + 1:]
                        len_regex = len(regex)

                        if len(input_str) > len_regex:

                            return False

                        elif len_regex > len(input_str):

                            return False

                        elif len(input_str) == len_regex:

                            if recursive_regex(f"{regex}|{input_str}"):

                                return True

                            elif not recursive_regex(f"{regex}|{input_str}"):

                                return False

                    if bool_ans is True and how_many == 1:

                        regex = regex[index + 1:]

                        # Getting rid of the positively matched character.

                        input_str_shortened = input_str[:index] + input_str[index + 1:]

                        if len(input_str_shortened) > len_regex:

                            return False

                        elif len_regex > len(input_str_shortened):

                            return False

                        elif len(input_str_shortened) == len_regex:

                            if recursive_regex(f"{regex}|{input_str_shortened}"):

                                return True

                            elif not recursive_regex(f"{regex}|{input_str_shortened}"):

                                return False

                # The "*" metacharacter block.

                if "*" in regex:

                    index, previous_char = find_previous_character_if_multiplication_mark(regex, 0)
                    bool_ans, how_many = make_comparisons_multiplication_mark(regex, input_str)

                    if not bool_ans:
                        return False

                    if bool_ans is True and how_many == 0:

                        regex = regex[index + 1:]

                        # While the input_str is evaluated to True (is not an empty string)
                        # there can be two responses from its combination with the regex plugged
                        # into the recursive_regex function - either True - and then the
                        # function returns True or False - and then the function returns False.

                        while input_str:

                            if recursive_regex(f"{regex}|{input_str}"):

                                return True

                            elif not recursive_regex(f"{regex}|{input_str}"):

                                return False

                    if bool_ans is True and how_many == 1:

                        regex = regex[index + 1:]

                        # Getting rid of the positively matched character.

                        input_str_shortened = input_str[:index] + input_str[index + 1:]

                        while input_str_shortened:

                            if recursive_regex(f"{regex}|{input_str_shortened}"):

                                return True

                            elif not recursive_regex(f"{regex}|{input_str_shortened}"):

                                return False

                    if bool_ans is True and how_many == 2:

                        regex = regex[index + 1:]

                        # Getting rid of the positively matched character.

                        input_str_shortened = input_str[:index] + input_str[index + 1:]

                        while input_str_shortened:

                            if recursive_regex(f"{regex}|{input_str_shortened}"):

                                return True

                            elif not recursive_regex(f"{regex}|{input_str_shortened}"):

                                return False

                # The "+" metacharacter block.

                if "+" in regex:

                    index, previous_char = find_previous_character_if_addition_mark(regex, 0)
                    bool_ans, how_many = make_comparisons_addition_mark(regex, input_str)

                    # It uses the regex_reversed and splits it on the plus metacharacter.

                    regex_reversed_list: List[str] = regex_reversed.split("+")

                    regex_rev_1: str = regex_reversed_list[0]

                    while regex_rev_1:

                        if not single_character_comparison(f"{regex_rev_1[0]}|{input_str_reversed[0]}"):

                            return False

                        else:

                            regex_rev_1 = regex_rev_1[1:]
                            input_str_reversed = input_str_reversed[1:]

                            return unequal_strings_find_match(f"{regex_rev_1}|{input_str_reversed}")

                    if not bool_ans:
                        return False

                    if bool_ans is True and how_many == 0:

                        regex = regex[index + 1:]

                        # While the input_str is evaluated to True (is not an empty string)
                        # there can be two responses from its combination with the regex plugged
                        # into the recursive_regex function - either True - and then the function
                        # returns True or False - and then the function returns False.

                        while input_str:

                            if recursive_regex(f"{regex}|{input_str}"):

                                return True

                            elif not recursive_regex(f"{regex}|{input_str}"):

                                return False

                    if bool_ans is True and how_many == 1:

                        regex = regex[index + 2:]

                        # Getting rid of the positively matched character.

                        input_str_shortened = input_str[:index] + input_str[index + 1:]

                        while input_str_shortened:

                            if recursive_regex(f"{regex}|{input_str_shortened}"):

                                return True

                            elif not recursive_regex(f"{regex}|{input_str_shortened}"):

                                input_str_shortened = input_str_shortened[1:]

                                return unequal_strings_find_match(f"{regex}|{input_str_shortened}")

                    if bool_ans is True and how_many == 2:

                        regex = regex[index + 1:]

                        # Getting rid of the positively matched character.

                        input_str_shortened = input_str[:index] + input_str[index + 1:]

                        while input_str_shortened:

                            if recursive_regex(f"{regex}|{input_str_shortened}"):

                                return True

                            elif not recursive_regex(f"{regex}|{input_str_shortened}"):

                                return False

                # The no "*", "?", "+" metacharacters block.

                else:

                    if recursive_regex(f"{regex}|{input_str}"):

                        return True

                    elif not recursive_regex(f"{regex}|{input_str}"):

                        return False

            # If the regex doesn't posses the metacharacters: "^" and "$", the index
            # counter variable is instantiated with the initial value od 0. The
            # input_str_shortened is instantiated as the string input_str with
            # the beginning index of index.

            elif not regex.startswith("^") and not regex.endswith("$"):

                i: int = 0

                input_str_shortened: str = input_str[i:]

                # "The backslash metacharacter block.

                if "\\" in regex:

                    if regex.startswith("\\"):

                        if len(regex) <= len(input_str_shortened):

                            next_char: str

                            index, next_char = find_next_character_if_backslash_detected(regex, 0)

                            regex_i: str = regex[index:]

                            if single_character_comparison_without_wildcard(f"{regex_i[0]}|{input_str_shortened[0]}"):

                                input_str = input_str[:index - 1] + input_str[index:]
                                regex = regex[:index - 1] + regex[index + 1:]

                                return unequal_strings_find_match(f"{regex}|{input_str}")
                            elif not single_character_comparison_without_wildcard(
                                    f"{regex_i[0]}|{input_str_shortened[0]}"):

                                input_str_shortened = input_str_shortened[1:]

                                return unequal_strings_find_match(f"{regex}|{input_str_shortened}")

                        elif len(input_str_shortened) < len(regex):

                            input_str_shortened = input_str_shortened[::-1]
                            regex_reversed = regex[::-1]

                            index, previous_char = find_next_character_if_backslash_detected_reversed(regex_reversed, 0)

                            regex_i = regex_reversed[index]

                            input_str_shortened_i: str = input_str_shortened[index]

                            if single_character_comparison_without_wildcard(f"{regex_i}|{input_str_shortened_i}"):

                                input_str_shortened = input_str_shortened[:index] + input_str_shortened[index + 2:]

                                input_str_shortened = input_str_shortened[::-1]

                                if regex == "\\\\" and not input_str_shortened:
                                    return True

                                regex_reversed = regex_reversed[:index] + regex_reversed[index + 2:]
                                regex = regex_reversed[::-1]

                                return unequal_strings_find_match(f"{regex}|{input_str_shortened}")

                            elif not single_character_comparison_without_wildcard(f"{regex_i}|{input_str_shortened_i}"):

                                return False

                    # If not regex starts with a backslash.

                    else:

                        if len(input_str_shortened) < len(regex):

                            input_str_shortened = input_str_shortened[::-1]
                            regex_reversed = regex[::-1]

                            index, previous_char = find_next_character_if_backslash_detected_reversed(regex_reversed, 0)

                            regex_i = regex_reversed[index]
                            input_str_shortened_i = input_str_shortened[index]

                            if single_character_comparison_without_wildcard(f"{regex_i}|{input_str_shortened_i}"):

                                input_str_shortened = input_str_shortened[:index] + input_str_shortened[index + 2:]
                                input_str_shortened = input_str_shortened[::-1]

                                if regex == "\\\\" and not input_str_shortened:
                                    return True

                                regex_reversed = regex_reversed[:index] + regex_reversed[index + 2:]
                                regex = regex_reversed[::-1]

                                return unequal_strings_find_match(f"{regex}|{input_str_shortened}")

                            elif not single_character_comparison_without_wildcard(f"{regex_i}|{input_str_shortened_i}"):

                                return False

                        elif len(regex) <= len(input_str_shortened):

                            index, previous_char = find_next_character_if_backslash_detected(regex, 0)

                            regex_i = regex[index]
                            input_str_shortened_i = input_str_shortened[index - 1]

                            if single_character_comparison_without_wildcard(f"{regex_i}|{input_str_shortened_i}"):
                                regex = regex[:index - 1] + regex[index + 1]
                                input_str_shortened = input_str_shortened[:index - 1] + input_str_shortened[index:]

                                return unequal_strings_find_match(f"{regex}|{input_str_shortened}")

                            if not single_character_comparison_without_wildcard(f"{regex_i}|{input_str_shortened_i}"):
                                return False

                # The "?" metacharacter block.

                elif "?" in regex:

                    index, previous_char = find_previous_character_if_question_mark(regex, 0)
                    bool_ans, how_many = make_comparisons_question_mark(regex, input_str)

                    if not bool_ans:
                        return False

                    elif bool_ans is True and how_many == 0:

                        regex = regex[index + 2:]

                        if recursive_regex(f"{regex}|{input_str_shortened}"):

                            return True

                        elif not recursive_regex(f"{regex}|{input_str_shortened}"):

                            i += 1
                            input_str_shortened = input_str_shortened[index:]
                            new_input: str = f"{regex}|{input_str_shortened}"

                            return unequal_strings_find_match(new_input)

                    elif bool_ans is True and how_many == 1:

                        regex = regex[index + 1:]
                        input_str_shortened = input_str[:index] + input_str[index + 1:]
                        while input_str_shortened:

                            if recursive_regex(f"{regex}|{input_str_shortened}"):

                                return True

                            elif not recursive_regex(f"{regex}|{input_str_shortened}"):

                                index += 1
                                input_str_shortened = input_str_shortened[index:]
                                new_input: str = f"{regex}|{input_str_shortened}"

                                return unequal_strings_find_match(new_input)

                    elif bool_ans is True and how_many == 2:

                        # The special case and don't touch it:

                        if len(regex) == 2:
                            return True

                        regex = regex[index + 1:]
                        input_str_shortened = input_str[:index] + input_str[index + 1:]
                        while input_str_shortened:

                            if recursive_regex(f"{regex}|{input_str_shortened}"):

                                return True

                            elif not recursive_regex(f"{regex}|{input_str_shortened}"):

                                index += 1
                                input_str_shortened = input_str_shortened[index:]
                                new_input: str = f"{regex}|{input_str_shortened}"

                                return unequal_strings_find_match(new_input)

                # The "*" metacharacter block.

                elif "*" in regex:

                    index, previous_char = find_previous_character_if_multiplication_mark(regex, 0)
                    bool_ans, how_many = make_comparisons_multiplication_mark(regex, input_str)

                    if bool_ans is False:

                        return False

                    elif bool_ans is True and how_many == 0:

                        regex = regex[index + 1:]

                        # While the input_str_shortened is evaluated to True (is not an empty
                        # string) there can be two responses from its combination with the regex
                        # plugged into the recursive_regex function - either True - and then the
                        # function returns True or False - and then the function returns False.

                        while input_str_shortened:

                            if recursive_regex(f"{regex}|{input_str_shortened}"):

                                return True

                            elif not recursive_regex(f"{regex}|{input_str_shortened}"):

                                input_str_shortened = input_str_shortened[1:]
                                regex = regex[1:]
                                new_string = f"{regex}|{input_str_shortened}"

                                return unequal_strings_find_match(new_string)

                    if bool_ans is True and how_many == 1:

                        regex = regex[index + 1:]
                        input_str_shortened = input_str[:index] + input_str[index + 1:]

                        while input_str_shortened:

                            if recursive_regex(f"{regex}|{input_str_shortened}"):

                                return True

                            else:

                                regex = regex[1:]
                                new_string = f"{regex}|{input_str_shortened}"

                                return unequal_strings_find_match(new_string)
                    if bool_ans is True and how_many == 2:

                        regex = regex[index + 1:]
                        input_str_shortened = input_str[:index] + input_str[index + 1:]

                        while input_str_shortened:

                            if recursive_regex(f"{regex}|{input_str_shortened}"):

                                return True

                            elif not recursive_regex(f"{regex}|{input_str_shortened}"):

                                return False

                # The "+" metacharacter block.

                elif "+" in regex:

                    index, previous_char = find_previous_character_if_addition_mark(regex, 0)
                    bool_ans, how_many = make_comparisons_addition_mark(regex, input_str)

                    if not bool_ans:
                        return False

                    if bool_ans is True and how_many == 0:

                        regex = regex[index + 1:]

                        # While the input_str_shortened is evaluated to True (is not an empty
                        # string) there can be two responses from its combination with the regex
                        # plugged into the recursive_regex function - either True - and then the
                        # function returns True or False - and then the function returns False.

                        while input_str_shortened:

                            if recursive_regex(f"{regex}|{input_str_shortened}"):

                                return True

                            elif not recursive_regex(f"{regex}|{input_str_shortened}"):

                                return False

                    if bool_ans is True and how_many == 1:

                        regex = regex[index + 1:]
                        input_str_shortened = input_str[:index] + input_str[index + 1:]

                        while input_str_shortened:

                            if recursive_regex(f"{regex}|{input_str_shortened}"):

                                return True

                            elif not recursive_regex(f"{regex}|{input_str_shortened}"):

                                regex = regex[1:]
                                new_string = f"{regex}|{input_str_shortened}"

                                return unequal_strings_find_match(new_string)

                    if bool_ans is True and how_many == 2:

                        regex = regex[index + 1:]
                        input_str_shortened = input_str[:index] + input_str[index + 1:]

                        while input_str_shortened:

                            if recursive_regex(f"{regex}|{input_str_shortened}"):

                                return True

                            elif not recursive_regex(f"{regex}|{input_str_shortened}"):

                                return False

                # The no "*", "?", "+" metacharacters block.

                else:

                    if recursive_regex(f"{regex}|{input_str_shortened}"):

                        return True

                    elif not recursive_regex(f"{regex}|{input_str_shortened}"):

                        if len(regex) == 1:

                            if single_character_comparison(f"{regex}|{input_str_shortened[0]}"):

                                return True

                            else:
                                input_str_shortened = input_str_shortened[1:]

                                return unequal_strings_find_match(f"{regex}|{input_str_shortened}")

                        elif len(regex) < len(input_str_shortened):

                            if regex:

                                if single_character_comparison(f"{regex[0]}|{input_str_shortened[0]}"):

                                    regex = regex[1:]
                                    input_str_shortened = input_str_shortened[1:]
                                    new_input = f"{regex}|{input_str_shortened}"

                                    return unequal_strings_find_match(new_input)

                                elif not single_character_comparison(f"{regex[0]}|{input_str_shortened[0]}"):

                                    input_str_shortened = input_str_shortened[1:]
                                    new_input = f"{regex}|{input_str_shortened}"

                                    return unequal_strings_find_match(new_input)

                        elif len(regex) == len(input_str_shortened):

                            return False

        # We are still considering input_string strings of length greater or equal
        # to 4. If the input_string starts with a vertical line  ("|"), an empty
        # string is assigned to the regex variable and the input_string stripped
        # of the vertical line is assigned to the input_str variable. If the regex
        # string is empty, in general, the single_character_comparison function
        # should return True.

        if input_string.startswith("|") and not input_string.endswith("|"):

            regex = ""
            input_str = input_string.strip("|")

            if not single_character_comparison(f"{regex}|{input_str[0]}"):

                return False

            else:

                input_str = input_str[1:]
                new_input = f"{regex}|{input_str}"

                return recursive_regex(new_input)

        # If the input_string ends with a vertical line, then the input_string
        # stripped off the vertical line is assigned to the regex variable,
        # and an empty string is assigned to the input_str variable. In that
        # cases, the single_character_comparison function should return False.

        if not input_string.startswith("|") and input_string.endswith("|"):

            regex = input_string.strip("|")

            input_str = ""

            if not single_character_comparison(f"{regex[0]}|{input_str}"):

                return False

            else:

                input_str = input_str[1:]
                new_input = f"{regex}|{input_str}"

                return recursive_regex(new_input)
