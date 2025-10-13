# https://www.codewars.com/kata/5808e2006b65bff35500008f/train/python

# When provided with a letter, return its position in the alphabet.

# Input :: "a"

# Output :: "Position of alphabet: 1"

# Note: Only lowercased English letters are tested

def position(letter):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return "Position of alphabet: " + str(alphabet.index(letter) + 1)
#
# def position(letter):
#     return "Position of alphabet: {}".format(ord(letter) - 96)
