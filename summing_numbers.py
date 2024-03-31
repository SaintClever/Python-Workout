def mysum(*nums):
    total = 0

    for num in nums:
        total += num

    return total


print(mysum(1, 2, 3))
print(mysum(10, 20, 30, 40, 50))
