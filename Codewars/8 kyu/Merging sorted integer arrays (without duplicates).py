# https://www.codewars.com/kata/573f5c61e7752709df0005d2/train/python

# Write a function that merges two sorted arrays into a single one. The arrays only contain integers. Also, the final outcome must be sorted and not have any duplicate.

def merge_arrays(first, second):
    res = first + second
    res.sort()
    print(res)

    for i in range(len(res) - 1, 0, -1):
        if res[i] == res[i - 1]:
            del res[i]

    return res
#
# def merge_arrays(a, b): 
#     return sorted(set(a + b))