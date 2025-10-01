# https://www.codewars.com/kata/5769b3802ae6f8e4890009d2/train/python

# Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

# None of the arrays will be empty, so you don't have to worry about that!

def remove_every_other(my_list):
    counter = len(my_list)
    
    while counter:
        if counter % 2 == 0:
            my_list.pop(counter - 1)
        counter -= 1

    return my_list

print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))  # ['Hello', 'Hello Again'])
print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # [1, 3, 5, 7, 9])
# 
def remove_every_other(my_list):
    return my_list[::2]