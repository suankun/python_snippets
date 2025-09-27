# https://www.codewars.com/kata/5866fc43395d9138a7000006/train/python

# Given a string, write a function that returns the string with a question mark ("?") appends to the end, unless the original string ends with a question mark, in which case, # # returns the original string.

# For example (Input --> Output)

# "Yes" --> "Yes?" 
# "No?" --> "No?"

def ensure_question(s):
    if len(s) == 0:
        return '?'
    return s if s[-1] == '?' else s + '?'
#
def ensure_question(s):
    return s if s.endswith('?') else s + '?'