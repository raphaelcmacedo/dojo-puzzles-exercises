# Exercisie extracted from
# http://dojopuzzles.com/problemas/exibe/ano-bissexto/
# Given an positive integer number return if it's a leap year or not
# It's a leap year if it is divisible by 4 but not divisible by 100 unless it is also divisible by 400

def play (year):
    leap_year = bool(not year % 4) and (bool(year % 100) or bool(not year % 400))
    return leap_year
