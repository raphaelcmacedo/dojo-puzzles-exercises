# Exercise propose in the module 2 of the course WTTD
# Given an positive integer number
# Replace the number by the sum of the squares of the digits
# If the result is 1 it's a happy nunmber
# Otherwise repeat the process
# The numbers resulting are happy, the others are sad


def sum_squares(number):
    return sum(int(char) ** 2 for char in str(number))


def play (number):
    already_tested = []
    while number != 1 and number not in already_tested:
        already_tested.append(number)
        number = sum_squares(number)

    return number == 1