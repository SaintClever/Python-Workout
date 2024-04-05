# def hex_output():
#     decnum = 0
#     hexnum = input("Enter a hex number to convert:")

#     for power, digit in enumerate(reversed(hexnum)):
#         decnum += int(digit, 16) * (16**power)
#         print(decnum)


# hex_output()


def hex_output(hexnum):
    return sum(
        int(digit, 16) * (16**power)
        for power, digit in enumerate(reversed(str(hexnum)))
    )


print(hex_output(100))
