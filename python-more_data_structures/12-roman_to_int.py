#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str:
        return 0
    dict_rom = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    value = 0
    for x in range(len(roman_string)):
        if x > 0 and dict_rom[roman_string[x]] > dict_rom[roman_string[x - 1]]:
            value -= dict_rom[roman_string[x - 1]] * 2
        value += dict_rom[roman_string[x]]
    return value
