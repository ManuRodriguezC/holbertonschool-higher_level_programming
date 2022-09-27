#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str:
        return 0
    value = 0
    for x in range(len(roman_string)):
        if roman_string[x] == 'I':
            value += 1
        elif roman_string[x] == 'V':
            if x > 0 and roman_string[x - 1] == 'I':
                value -= 2
            value += 5
        elif roman_string[x] == 'X':
            if x > 0 and roman_string[x - 1] == 'I':
                value -= 2
            elif x > 0 and roman_string[x - 1] == 'V':
                value -= 10
            value += 10
        elif roman_string[x] == 'L':
            if x > 0 and roman_string[x - 1] == 'I':
                value -= 2
            elif x > 0 and roman_string[x - 1] == 'V':
                value -= 10
            elif x > 0 and roman_string[x - 1] == 'X':
                value -= 20
            value += 50
        elif roman_string[x] == 'C':
            if x > 0 and roman_string[x - 1] == 'I':
                value -= 2
            elif x > 0 and roman_string[x - 1] == 'V':
                value -= 10
            elif x > 0 and roman_string[x - 1] == 'X':
                value -= 20
            elif x > 0 and roman_string[x - 1] == 'L':
                value -= 100
            value += 100
        elif roman_string[x] == 'D':
            if x > 0 and roman_string[x - 1] == 'I':
                value -= 2
            elif x > 0 and roman_string[x - 1] == 'V':
                value -= 10
            elif x > 0 and roman_string[x - 1] == 'X':
                value -= 20
            elif x > 0 and roman_string[x - 1] == 'L':
                value -= 100
            elif x > 0 and roman_string[x - 1] == 'C':
                value -= 200
            value += 500
        elif roman_string[x] == 'M':
            if x > 0 and roman_string[x - 1] == 'I':
                value -= 2
            elif x > 0 and roman_string[x - 1] == 'V':
                value -= 10
            elif x > 0 and roman_string[x - 1] == 'X':
                value -= 20
            elif x > 0 and roman_string[x - 1] == 'L':
                value -= 100
            elif x > 0 and roman_string[x - 1] == 'C':
                value -= 200
            elif x > 0 and roman_string[x - 1] == 'D':
                value -= 1000
            value += 1000
    return value
