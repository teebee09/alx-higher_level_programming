#!/usr/bin/python3

def best_score(a_dictionary):
    highest_key = 0
    highest_value = None
    if a_dictionary:
        for key, value in a_dictionary.items():
            if value > biggest_value:
                highest_value = value
                highest_key = key
    return highest_key
