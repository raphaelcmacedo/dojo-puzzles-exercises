# Exercisie extracted from
# http://dojopuzzles.com/problemas/exibe/encontre-o-telefone/
#In some places it is common to remember a phone number associating its digits to letters. Thus the expression MY LOVE means 69 5683.
# Of course there are some problems, since some phones do not form a word or a phrase and the digits 1 and 0 are not associated with any letter.
#Your task is to read an expression and find the corresponding phone number based on the table below.
# An expression consists of uppercase letters (A-Z), hyphens (-) and the numbers 1 and 0.


_phone_keys = [
    (('A,B,C'), '2'),
    (('D,E,F'), '3'),
    (('G,H,I'), '4'),
    (('J,K,L'), '5'),
    (('M,N,O'), '6'),
    (('P,Q,R,S'), '7'),
    (('T,U,V'), '8'),
    (('W,X,Y,Z'), '9'),
]

def letter_to_number(char):
    for key in _phone_keys:
        if str(char) in key[0]:
            return key[1]


def convert (expression):
    result = ''
    for char in expression:
        if str(char).isalpha():
            result += letter_to_number(char)
        else:
            result += str(char)

    return result

