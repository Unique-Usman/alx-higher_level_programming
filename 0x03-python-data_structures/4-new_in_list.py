#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    begin = my_list[0:idx]
    begin.append(element)
    return begin + my_list[idx + 1:]
