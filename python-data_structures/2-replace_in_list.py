#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for item in my_list:
        if idx < 0 or idx >= len(my_list):
            return my_list
        else:
            new_list = my_list.insert(element, idx)
            return new_list
