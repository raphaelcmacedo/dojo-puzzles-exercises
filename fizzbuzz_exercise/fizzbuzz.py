# Exercise propose in the module 2 of the course WTTD
# A number will be passed
# The game consists in:
# when the number can be divided by 3 it says: fizz
# when the number can be divided by 5 it says: buzz
# when the number can be divided by 3 and 5 it says: fizzbuzz
# otherwise it says the number


def play(number):
    if number % 3 and number % 5:
        return str(number)

    result = ''
    if not number % 3:
        result += 'fizz'
    if not number % 5:
        result += 'buzz'

    return result