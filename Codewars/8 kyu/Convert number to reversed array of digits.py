# https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python

# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

# Example (Input => Output):
# 35231 => [1,3,2,5,3]
# 0     => [0]

def digitize(n):
    rev_list = []
    num_to_str = str(n)

    for ch in num_to_str:
        rev_list.append(int(ch))

    print(rev_list)
    rev_list.reverse()

    return rev_list
#
def digitize(n):
    return [int(x) for x in str(n)[::-1]]
