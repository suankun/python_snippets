# https://www.codewars.com/kata/58dbdccee5ee8fa2f9000058/train/python

# Given a string of arbitrary length with any ascii characters. Write a function to determine whether the string contains the whole word "English".
#
# The order of characters is important -- a string "abcEnglishdef" is correct but "abcnEglishsef" is not correct.
#
# Upper or lower case letter does not matter -- "eNglisH" is also correct.
#
# Return value as boolean values, true for the string to contains "English", false for it does not.

def sp_eng(sentence):
    sentence_to_lower = sentence.lower()
    index = sentence_to_lower.find("english")
    return True if index != -1 else False
#
def sp_eng(sentence):
    return 'english' in sentence.lower()

sp_eng("english")               # True
sp_eng("egnlish")               # False
sp_eng("engliish")              # False
sp_eng("1234egn lis;h")         # False
sp_eng("1234english ;k")        # True
sp_eng("English")               # True
sp_eng("eNgliSh")               # True
sp_eng("1234#$%%eNglish ;k9")   # True
sp_eng("EGNlihs")               # False
sp_eng("1234englihs**")         # False
