"""
Write a function, called how_many_different_numbers, that  takes a single list of integers and returns the number of different integers it contains. 
"""


def how_many_different_numbers(num):
    # return list(set(num))
    return list({*num})


numbers = [1, 2, 3, 1, 2, 3, 4, 1]
print(how_many_different_numbers(numbers))
