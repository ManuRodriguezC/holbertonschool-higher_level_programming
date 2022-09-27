#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key = a_dictionary.value('value')
    del a_dictionary[key]
