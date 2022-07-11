# Problem 17:
#     Number Letter Counts
#
# Description:
#     If the numbers 1 to 5 are written out in words:
#       * one,
#       * two,
#       * three,
#       * four,
#       * five,
#     then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
#     If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
#       how many letters would be used?
#
#     NOTE:
#       Do not count spaces or hyphens.
#       For example,
#         342 (three hundred and forty-two) contains 23 letters and
#         115 (one hundred and fifteen) contains 20 letters.
#       The use of "and" when writing out numbers is in compliance with British usage.

from num2words import num2words


def letter_count(s):
    """
    Returns the count of letters only in given string `s`.

    Args:
        s (str): Any string

    Returns:
        Count of letters in `s`
    """
    return len(list(filter(lambda c: c.isalpha(), list(s))))


def main(n: int) -> int:
    """
    Returns the total count of letters used while
      writing all the numbers 1 to `n` (inclusive) in words.
    Note that word form of numbers is in compliance with *British* usage.

    Args:
        n (int): Natural number

    Returns:
        (int): Total count of letters in 1 to `n` (inclusive) when written as words

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(n) == int and n > 0

    # Just iterate all the numbers and count the letters.
    # There's probably a smarter way to do this, but whatever.
    count = 0
    for i in range(n):
        # Apparently there's a Python lib that already does this for you
        word = num2words(i+1, lang='en_GB')
        count += letter_count(word)
    return count


if __name__ == '__main__':
    num = int(input('Enter a natural number: '))
    total_count = main(num)
    print('Number of letters needed to write numbers 1 to {} as words'.format(num))
    print('  {}'.format(total_count))
