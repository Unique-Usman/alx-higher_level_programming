#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    real_max = 0
    real_key = ""
    count = 0
    for i in a_dictionary.keys():
        tmp_max = a_dictionary[i]
        tmp_dict = i
        if count == 0:
            real_max = tmp_max
            real_key = tmp_dict
        if tmp_max > real_max:
            real_max = tmp_max
            real_key = i
        count += 1
    return real_key
