#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str:
        return 0
    value = 0
    for x in range(len(roman_string)):
        if roman_string[x] == 'I':
            value += 1
        elif roman_string[x] == 'V':
            value += 5
        elif roman_string[x] == 'X':
            value += 10
        elif roman_string[x] == 'L':
            value += 50
        elif roman_string[x] == 'C':
            value += 100
        elif roman_string[x] == 'D':
            value += 500
        elif roman_string[x] == 'M':
            value += 1000
    return value
