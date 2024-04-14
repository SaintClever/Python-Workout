"""
So far, we've worked with individual files. Many tasks, however, require you to analyze  data in multiple files—such as all of the files in a dict. This exercise will give you some  practice working with multiple files, aggregating measurements across all of them.

In this exercise, write two functions. find_longest_word takes a filename as an  argument and returns the longest word found in the file. The second function, find_all_longest_words, takes a directory name and returns a dict in which the keys are  filenames and the values are the longest words from each file.

If you don't have any text files that you can use for this exercise, you can download  and use a zip file I've created from the five most popular books at Project Gutenberg  (https://gutenberg.org/). You can download the zip file from http://mng.bz/rrWj.

NOTE: There are several ways to solve this problem. If you already know how  to use comprehensions, and particularly dict comprehensions, then that's  probably the most Pythonic approach. But if you aren't yet comfortable with  them, and would prefer not to jump to read about them in chapter 7, then no  worries—you can use a traditional for loop, and you'll be just fine.
"""

import pprint, os


def find_all_longest_words(dir):
    output = {}

    # Get file paths and extract content of files into book dict
    for root, _, files in os.walk(dir):
        for file in files:
            with open(root + file) as f:
                books = f.read()

                # Loop thru book content and sanitize words
                words = "".join(i for i in books).split()

                # Sanitize words
                count = 0
                for word in words:
                    if (
                        len(word) > count
                        and "http" not in word
                        and "www" not in word
                        and "trademark" not in word
                        and "-" not in word
                        and "_" not in word
                        and "@" not in word
                        and "&" not in word
                        and "?—" not in word
                        and "—" not in word
                    ):
                        count = len(word)
                        output[file] = [{word: count}]

    return output


pprint.pprint(find_all_longest_words("books/"))
