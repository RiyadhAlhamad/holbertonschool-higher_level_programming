#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list = my_list[:]
    if (idx < 0 or idx > len(my_list)-1):
        return list
    else:
        for i in range(len(my_list)):
            if (i == idx):
                list[i] = element
        return list
