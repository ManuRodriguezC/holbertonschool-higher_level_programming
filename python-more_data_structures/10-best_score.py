#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        value_max = max(a_dictionary, key=lambda x: a_dictionary[x])
        return value_max
    return None
