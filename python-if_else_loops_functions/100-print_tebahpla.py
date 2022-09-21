#!/usr/bin/python3
for letter in reversed(range(65, 91)):
    if letter % 2 == 0:
        print("{:c}".format(letter + 32), end="")
    else:
        print("{:c}".format(letter), end="")
