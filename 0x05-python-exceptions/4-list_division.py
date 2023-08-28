#!/usr/bin/python3


def list_division(my_list_1: list, my_list_2: list, list_length: list) -> list:
    new_list = []
    for i in range(list_length):
        ans = 0
        try:
            ans = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong Type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(ans)
    return new_list
