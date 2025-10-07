# https://www.codewars.com/kata/5208f99aee097e6552000148/train/python
#
# Complete the solution so that the function will break up camel casing, using a space between words.
#
# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

def solution(s):
    res = ""
    for ch in s:
        if ch.isupper():
            res += " " + ch
        else:
            res += ch
    return res
#
# def solution(s):
#     return ''.join(' ' + c if c.isupper() else c for c in s)