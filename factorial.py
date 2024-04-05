def factorial(num):
    total = 1
    for i in range(1, num + 1):
        total *= i
    return total


print(factorial(5))
