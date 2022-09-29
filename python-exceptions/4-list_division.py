#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    pos = 0
    while pos < list_length:
        try:
            value = my_list_1[pos] / my_list_2[pos]
        except IndexError:
            print("out of range")
            value = 0
        except ZeroDivisionError:
            print("division by 0")
            value = 0
        except TypeError:
            print("wrong type")
            value = 0
        finally:
            new.append(value)
            pos += 1
    return new
