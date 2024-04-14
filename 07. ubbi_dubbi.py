def ubbi_dubbi(string) -> str:
    vowels = "aeiou"
    # output = ""

    # for vowel in string:
    #     if vowel in vowels:
    #         output += f"ub{vowel}"
    #     else:
    #         output += vowel

    # return output

    return "".join(f"ub{vowel}" if vowel in vowels else vowel for vowel in string)


print(ubbi_dubbi("octopus"))
print(ubbi_dubbi("elephant"))
