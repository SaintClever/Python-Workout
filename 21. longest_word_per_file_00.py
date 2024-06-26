"""
So far, we've worked with individual files. Many tasks, however, require you to analyze  data in multiple files—such as all of the files in a dict. This exercise will give you some  practice working with multiple files, aggregating measurements across all of them.

In this exercise, write two functions. find_longest_word takes a filename as an  argument and returns the longest word found in the file. The second function, find_all_longest_words, takes a directory name and returns a dict in which the keys are  filenames and the values are the longest words from each file.

If you don't have any text files that you can use for this exercise, you can download  and use a zip file I've created from the five most popular books at Project Gutenberg  (https://gutenberg.org/). You can download the zip file from http://mng.bz/rrWj.

NOTE: There are several ways to solve this problem. If you already know how  to use comprehensions, and particularly dict comprehensions, then that's  probably the most Pythonic approach. But if you aren't yet comfortable with  them, and would prefer not to jump to read about them in chapter 7, then no  worries—you can use a traditional for loop, and you'll be just fine.
"""

import string


def find_longest_word(file):
    # Open file
    with open("books/43-0.txt") as f:
        file = f.read()

        # Clean text
        words = "".join(i for i in file if i not in string.punctuation).split()

        # Additional cleansing of words and populate & return dict below
        word, count = "", 0
        for wrd in words:
            if (
                len(wrd) > count
                and "http" not in wrd
                and "www" not in wrd
                and "—" not in wrd
            ):
                count = len(wrd)
                word = wrd

        return {word: count}


print(find_longest_word("books/43-0.txt"))
