#!/usr/bin/python3

def best_score(a_dictionary):
    highest_value = 0
    highest_key = None
    if a_dictionary:
        for key, value in a_dictionary.items():
            if value > highest_value:
                highest_value = value
                highest_key = key
    return highest_key
