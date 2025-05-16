#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set(my_list)
    result = 0
    for number in unique_set:
        result += number
    return result
