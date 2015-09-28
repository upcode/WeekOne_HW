"""Skills Assessment: Lists.

To work on an item, uncomment the entire function (including the docstring)
and then run this script. It should output an error that the newly-uncommented
function is now failing its tests.

Edit the function body until you have a solution and the test passes, and then
move on to the next function.

This assessment is DUE TO YOUR ADVISOR BY SUNDAY EVENING.
"""


def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []

    """
    #steps
    #create a new list
    #find odds by iterating through list
    #once we find odds append odd numbers to new list
    #return new list

    odd_list = []  # created a new list for odd numbers
    for number in number_list:  # looking number_list for numbers that are odd
        if number % 2 != 0:  # if numbers are divisable by two any even numbers stay
            odd_list.append(number)  # if numbers are odd, append those odd numbers to the back of our odd_list
    return odd_list  # return odd_list


def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """
    even_list = []  # create new empty list for even numbers to append too
    for number in number_list:  # iterating through the list for numbers in number_list
        if number % 2 == 0:  # if numbers are divisval by 2 and equal too even then append numbers
            even_list.append(number)  # append even numbers to the back of even_list
    return even_list  # return even_list


def print_indeces(my_list):
    """Print the index of each list item, followed by the item itself.
    Do this without using a counting variable. I.e. don't do something
    like this:

    count = 0
    for item in list:
        print count
        count = count + 1

    Output should look like this:

    >>> print_indeces(["Toyota", "Jeep", "Volvo"])
    0 Toyota
    1 Jeep
    2 Volvo

    """
    for index, item in enumerate(my_list):  # enumerates prints index and items in list
        print index, item


def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """
    long_words_list = []  # created an empty list
    for word in word_list:  # iterating though words_list for words that longer then 4 characters
        if len(word) > 4:  # if length of words is greater then 4 characters
            long_words_list.append(word)  # append words longer then 4 chacaters to the back of long_word_list

    return long_words_list  # return long_word_list with words with characters longer then four


def smallest_int(number_list):

    smallest_num_seen_so_far = number_list[0]  # create variable for the smallest number ie place holder assign it to number list starting at 0
    for number in number_list:  # iterate list for number in number_list
        if number < smallest_num_seen_so_far:  # if number is smaller then previous number, then smallest number will be replaces by previus smallest number
            smallest_num_seen_so_far = number
    return smallest_number_seen_so_far  # return smallest number after iterating through list


def largest_int(number_list):

    largest_number_seen_so_far = number_list[0]  # created variable to hold largest number set ut to number list starting at index 0
    for number in number_list:  # iterate list for number in number list
        if number > largest_number_seen_so_far:  # number greater then previous number replace new larger number continue to iterate end of the list
            largest_number_seen_so_far = number

    return largest_number_seen_so_far  # returns largest int in list


def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """
    # control statements are for, while and if else elif followed by :
    halvesies_list = []  # created empty list to append numbers divided by two
    for number in number_list:  # iterate though number_list for number
        float_number = float(number) / 2  # created var float_number number divided by two
        halvesies_list.append(float_number)  # if number is divical by two append numbers to back of halveies list
    return halvesies_list  # return haveslies list of all numbers divisal by two


def word_lengths(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """
    word_length_list = []  #created empty list called word_length_list to append length of words to
    for word in word_list:  # iterate word_list for each word
        word_length_list.append(len(word))  # for each word in word_list append word to word_length_list once len of word is found
        return word_length_list  # return word_length_list with list of words with their lenghts


def sum_numbers(number_list):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does this -- but for
    this exercise, you should not use it.

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero:

        >>> sum_numbers([])
        0

    """
    total = 0  # this is my starting point this is where iteration should start
    for number in number_list:  #iterate number_list for numbers starting at 0
        total = total + number  # if total = previous total plus next number in list
    return total  # returns the total or sum of all numbers in number_list


def mult_numbers(number_list):
    """Return product (result of multiplication) of the numbers in the list.

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in the input, the product will be zero:

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product, if the list is
    empty, the product should be 1:

        >>> mult_numbers([])
        1

    """
    multi_numbers_total = 1  # starting point using starting at 1 and not mulitplying by 0 results moot point
    for number in number_list:  # iterate through number_list and for each number multiply each number by previous total
        multi_numbers_total = multi_numbers_total * number  # previous number becomes total and multiply new total by next number in list
    return multi_numbers_total  # return total of number_list


def join_strings(word_list):
    """Return a string of all input strings joined together.

    Python ha a built-in method on lists, `join` -- but this exercise, you
    should not use it.

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string:

        >>> join_strings([])
        ''

    """

    join_words = ""  # no space needed
    for word in word_list:
        join_words = join_words + word

    return join_words


def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.
    """

    total = 0  # this is my starting point
    for number in number_list:
        total = total + number
    return (float(total) / float(len(number_list))

#############################################################################
# END OF SKILLS TEST: You can stop here, or read on to work on advanced problem.

# Uncomment the function below to work on the advanced problem.
# Tip: To comment or uncomment blocks of code, highlight what you want to
#    comment or uncomment, and then CMD+"/" or CTRL-"/"

# def advanced_join_strings(list_of_words):
#     """Return a single string with each word from the input list
#     separated by a comma.

#         >>> advanced_join_strings(["Labrador", "Poodle", "French Bulldog"])
#         'Labrador, Poodle, French Bulldog'

#     If there's only one thing in the list, it should return just that
#     thing, of course:

#         >>> advanced_join_strings(["Pretzel"])
#         'Pretzel'

#     """

#     return ""

# END OF ASSIGNMENT: You can ignore everything below.
##############################################################################

if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s TESTS PASSED. GOOD WORK!" % result.attempted
    print
