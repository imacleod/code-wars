from itertools import groupby


def longest_repetition(chars):
    """ Determine character(s) with greatest repetition
    :return tuple of (longest repeating char, count) """

    return max(((char, len(list(group))) for char, group in groupby(chars)),
               key=lambda char_group: char_group[1],
               default=('', 0))


if __name__ == "__main__":
    print(longest_repetition(''))
    print(longest_repetition('ba'))
    print(longest_repetition('aaaabb'))
    print(longest_repetition('cbdeuuu900'))
