def most_repeating_word(strings):
    return "".join(set(i) for i in strings)


words = ["this", "is", "an", "elementary", "test", "example"]
print(most_repeating_word(words))
