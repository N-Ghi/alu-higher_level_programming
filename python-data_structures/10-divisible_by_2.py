#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return
    for item in my_list:
        if item % 2 != 0:
           print('{:d} is not divisible by 2'.format(item))
        else:
           print('{:d} is divisible by 2'.format(item))
