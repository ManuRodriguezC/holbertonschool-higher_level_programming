#!/usr/bin/python3
"""Module: 5-text_indentation"""


def text_indentation(text):
    """check if text is string"""
    if type(text) != str:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if text[i] == ":" or text[i] == "?" or text[i] == ".":
            print(text[i])
            print()
        if text[i] != " " or (text[i - 1] != "." and text[i - 1] != ":"
                              and text[i - 1] != "?" and text[i - 1] != " "):
            if text[i] != ":" and text[i] != "." and text[i] != "?":
                print(text[i], end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
