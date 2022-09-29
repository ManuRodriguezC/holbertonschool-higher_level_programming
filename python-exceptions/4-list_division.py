#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    if len(my_list_1) > len(my_list_2):
        new = my_lits_1.copy()
    else:
        new = my_list_2.copy()
    pos = 0
    while pos < list_length:
        try:
            new[pos] = my_list_1[pos] / my_list_2[pos]
        except IndexError:
            print("out of range")
            new[pos] = 0
        except ZeroDivisionError:
            print("division by 0")
            new[pos] = 0
        except TypeError:
            print("wrong type")
            new[pos] = 0
        finally:
            pos += 1
    return new
