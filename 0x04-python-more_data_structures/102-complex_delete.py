#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    emp = []
    for key, val in a_dictionary.items():
        if val == value:
            emp.append(key)
    for i in emp:
        del a_dictionary[i]
    return a_dictionary
