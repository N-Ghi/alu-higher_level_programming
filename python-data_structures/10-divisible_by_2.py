#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if not my_list:
        return
    for item in my_list:
        if item % 2 == 0:
            print("{:d} {:s} divisible by 2".format(item, "is"))
        else:
            print("{:d} {:s} divisible by 2".format(item, "is not"))
