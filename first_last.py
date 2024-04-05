"""
We’ll practice these ideas with this exercise. Write a function, firstlast, that takes  a sequence (string, list, or tuple) and returns the first and last elements of that  sequence, in a two-element sequence of the same type. So firstlast('abc') will  return the string ac, while firstlast([1,2,3,4]) will return the list [1,4]. 
"""


def first_last(sequence):
    return [sequence[0], *sequence[-1:]]


print(first_last([1, 2, 3, 4]))
print(first_last("Hello World!"))
print(first_last(("a", "b", "c")))
print(first_last(["Hello", "beautiful", "World!"]))
print(first_last(("Hello", "beautiful", "World!")))
