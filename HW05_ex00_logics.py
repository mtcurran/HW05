#!/usr/bin/env python
# HW05_ex00_logics.py
##############################################################################

def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    num = raw_input("Enter an integer: ")
    try:
        int(num)
    except:
        print "Try again, please enter a numeral integer."
    else:
        if (int(num) % 2) == 0:
            print "Even"
        else:
            print "Odd"
    return


def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    n = 1
    for row in range(10):
        for column in range(10):
            if n <= 10:
                print str(n) + " ",
            else:
                print str(n),
            n += 1
        print " "
    return


def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    numbers = []

    while True:
        num_input = raw_input("Enter a number: ")
        if num_input == "done":
            break
        try:
            float(num_input)
        except:
            print "Try again, please enter numerical inputs."
        else:
            numbers.append(num_input)

    numbers_total = 0.0
    i = 0
    while i < len(numbers):
        numbers_total += float(numbers[i])
        i += 1
    else:
        averaged_nums = float(numbers_total)/len(numbers)
    
    return averaged_nums

##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    #even_odd()
    #ten_by_ten()

    print find_average()

if __name__ == '__main__':
    main()
