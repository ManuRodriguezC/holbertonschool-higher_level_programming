#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            ch = chr(ord(letter) - 32)
        else:
            ch = letter
        print("{:s}".format(ch), end="")
    print("")
