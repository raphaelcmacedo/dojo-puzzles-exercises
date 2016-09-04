# Exercisie extracted from
# http://dojopuzzles.com/problemas/exibe/poker/

# In the game of poker, a hand consisting of five cards can be compared, from lowest to highest, as follows:
#
#     High Card: The highest card.
#     One pair: Two cards of the same value.
#     Two Pair: Two different pairs.
#     Kind: Three cards of one rank and two different values.
#     Straight (sequence): All letter with consecutive values.
#     Flush: All cards of the same suit.
#     Full House: A set and a pair.
#     Court: Four cards of the same value.
#     Straight Flush: All cards are consecutive and the same suit.
#     Royal Flush: The sequence 10, Jack, Queen, King, Ace of the same suit.
#
#     The letters are, in order of increasing value: 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack (J), Queen(Q), King(K), Ace(A).
#     The suits are: Gold (D), Cup (H), Swords (S), Wands (C)
#
#      Exmaples of valid hands:5H 5C 6S 7S KD	  	2C 3S 8S 8D TD     5D 8C 9S JS AC	  	2C 5C 7D 8S QH

def play (hand_player_1, hand_player_2):
    return None