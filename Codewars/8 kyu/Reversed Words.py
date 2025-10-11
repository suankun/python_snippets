# https://www.codewars.com/kata/51c8991dee245d7ddf00000e/train/python

# Complete the solution so that it reverses all of the words within the string passed in.

# Words are separated by exactly one space and there are no leading or trailing spaces.

# Example(Input --> Output):

# "The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"

def reverse_words(s):
    res = ""

    list_of_words = s.split()

    for word in list_of_words[::-1]:
        res += word + " "

    res = res[:-1]

    return res

print(reverse_words("The greatest victory is that which requires no battle"))  # "battle no requires which that is victory greatest The"
#
# def reverseWords(str):
#     return " ".join(str.split(" ")[::-1])