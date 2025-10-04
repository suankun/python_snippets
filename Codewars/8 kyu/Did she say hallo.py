# https://www.codewars.com/kata/56a4addbfd4a55694100001f/train/python

# Write a simple function to check if the string contains the word hallo in different languages.

# These are the languages of the possible people you met the night before:

# hello - english
# ciao - italian
# salut - french
# hallo - german
# hola - spanish
# ahoj - czech republic
# czesc - polish

# Notes
# you can assume the input is a string.
# to keep this a beginner exercise you don't need to check if the greeting is a subset of word (Hallowen can pass the test)
# function should be case insensitive to pass the tests

def validate_hello(greetings):
    greet_lower = greetings.lower()
    greet_list = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]
    for gr in greet_list:
        if gr in greet_lower:
            return True

    return False
           

# print(validate_hello('hello'))  # True
# print(validate_hello('ciao bella!'))  # True
# print(validate_hello('salut'))  # True
# print(validate_hello('hallo, salut')) # True
# print(validate_hello('hombre! Hola!'))  # True
# print(validate_hello('Hallo, wie geht\'s dir?'))  # True
# print(validate_hello('AHOJ!'))  # True
print(validate_hello('czesc'))  # True
print(validate_hello('meh'))  # False
print(validate_hello('Ahoj'))  # True

# def validate_hello(greetings):
#     return any(x in greetings.lower() for x in ['hello','ciao','salut','hallo','hola','ahoj','czesc'])