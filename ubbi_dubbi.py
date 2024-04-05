def ubbi_dubbi(string) -> str:
    vowels = "aeiou"
    # output = ""

    # for i in string:
    #     if i in vowels:
    #         output += f"ub{i}"
    #     else:
    #         output += i

    # return output

    return "".join(f"ub{i}" if i in vowels else i for i in string)


print(ubbi_dubbi("octopus"))
print(ubbi_dubbi("elephant"))
