from collections import Counter


def most_repeating_word(strings):
    # count = 0
    # char, output = "", ""

    # for word in strings:
    #     for letter in word:
    #         if word.count(letter) > count:
    #             count = word.count(letter)
    #             char = letter
    #             output = word

    # return f"{output}: with {count} {char.upper()!r}s"

    return Counter("".join(word for word in strings)).most_common(1)


words = ["this", "is", "racecar racer", "an", "elementary", "test", "example"]
print(most_repeating_word(words))
