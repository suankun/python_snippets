# https://www.codewars.com/kata/5808dcb8f0ed42ae34000031/train/python

# When provided with a number between 0-9, return it in words. Note that the input is guaranteed to be within the range of 0-9.

# Input: 1

# Output: "One".

def switch_it_up(number):
    res = ""
    if number == 0:
        res = "Zero"
    elif number == 1:
        res = "One"
    elif number == 2:
        res = "Two"
    elif number == 3:
        res = "Three"
    elif number == 4:
        res = "Four"
    elif number == 5:
        res = "Five"
    elif number == 6:
        res = "Six"
    elif number == 7:
        res = "Seven"
    elif number == 8:
        res = "Eight"
    elif number == 9:
        res = "Nine"
    return res
#
def switch_it_up(n):
    return ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine'][n]
