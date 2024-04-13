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


def word_count(file_name):
    output = {
        "characters": 0,  # 165
        "different_words": 0,  # 20
        "lines": 0,  # 11
        "new_line": 0,  # 11
        "whitespace": 0,  # 22
        "words": 0,  # 28
    }

    with open(file_name) as f:
        file = f.read()

    output["characters"] = len(file)
    output["different_words"] = len(set(file.split()))
    output["lines"] = len([sentence for sentence in file.strip().split("\n")])
    output["new_line"] = len([word for word in file if word == "\n"])
    output["whitespace"] = len([word for word in file if word == " "])
    output["words"] = len(set(file))

    return output


pprint(word_count("docs/wcfile.txt"))
