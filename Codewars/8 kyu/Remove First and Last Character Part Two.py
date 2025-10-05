# https://www.codewars.com/kata/570597e258b58f6edc00230d/train/python

# You are given a string containing a sequence of character sequences separated by commas.

# Write a function which returns a new string containing the same character sequences except the first and the last ones but this time separated by spaces.

# If the input string is empty or the removal of the first and last items would cause the resulting string to be empty, return an empty value (represented as a generic value NULL in the examples below).

# Examples
# "1,2,3"      =>  "2"
# "1,2,3,4"    =>  "2 3"
# "1,2,3,4,5"  =>  "2 3 4"

# ""     =>  None
# "1"    =>  None
# "1,2"  =>  None

def array(string):
    if len(string) == 0:
        return None
    
    list_of_numbers = string.split(",")
    
    if len(list_of_numbers) <= 2:
        return None
    
    list_of_numbers.pop(0)
    list_of_numbers.pop(len(list_of_numbers) - 1)
    res = ""
    for num in list_of_numbers:
        res += num + " "

    x = res.rstrip()
    
    return x
           

# print(array('1,2,3'))  # '2'
# print(array('1,2,3,4'))  # '2 3'
print(array('1,2,3,4,5'))  # '2 3 4'

# def array(strng):
#     return ' '.join(strng.split(',')[1:-1]) or None
