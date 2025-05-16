#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_key = None
    max_value = float('-inf')
    for i in a_dictionary:
        if a_dictionary[i] > max_value:
            max_value = a_dictionary[i]
            max_key = i

    return max_key
