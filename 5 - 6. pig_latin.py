"""
If the word begins with a vowel (a, e, i, o, or u), add “way” to the end of the  word. So “air” becomes “airway” and “eat” becomes “eatway.”

If the word begins with any other letter, then we take the first letter, put it on  the end of the word, and then add “ay.” Thus, “python” becomes “ythonpay”  and “computer” becomes “omputercay.” 
"""

# def pig_latin(string):
#     vowels = "aeiou"
#     output = ""

#     for word in string.split():
#         if word[0] in vowels:
#             output += f"{word}way "
#         else:
#             output += f"{word[1:]}{word[0]}ay "

#     return output.strip()


def pig_latin(string):
    # vowels = "aeiou"
    # output = []

    # for word in string.split():
    #     if word[0] in vowels:
    #         output.append(f"{word}way")
    #     else:
    #         output.append(f"{word[1:]}{word[0]}ay")

    # return " ".join(output)

    vowels = "aeiou"

    output = " ".join(
        f"{word}way" if word[0] in vowels else f"{word[1:]}{word[0]}ay"
        for word in string.split()
    )

    return output


print(pig_latin("this is a test translation"))
