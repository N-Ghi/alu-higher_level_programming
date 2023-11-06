#!/usr/bin/python3
def element_at(my_list, idx):
    for item in my_list:
        if idx < 0 or idx >= int(len(my_list)):
            return None
        else:
            x = my_list[idx]
            return x
