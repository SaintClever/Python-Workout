from pprint import pprint


"""
The challenge for this exercise is to write a wordcount function that mimics the wc  Unix command. The function will take a filename as input and will print four lines  of output:  1 Number of characters (including whitespace)  2 Number of words (separated by whitespace)  3 Number of lines  4 Number of unique words (case sensitive, so “NO” is different from “no”)


This is a test file.  

It contains 28 words and 20 different words.  

It also contains 165 characters.  

It also contains 11 lines.  

It is also self-referential.  

Wow! 
"""


def wordcount(filename):
    counts = {"characters": 0, "words": 0, "lines": 0}

    unique_words = set()

    for one_line in open(filename):
        counts["lines"] += 1
        counts["characters"] += len(one_line)
        counts["words"] += len(one_line.split())
        unique_words.update(one_line.split())
        counts["unique words"] = len(unique_words)

        for key, value in counts.items():
            print(f"{key}: {value}")


wordcount("docs/wcfile.txt")
