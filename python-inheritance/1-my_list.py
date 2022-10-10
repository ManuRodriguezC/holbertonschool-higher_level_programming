#!/usr/bin/python3


"""This class contein all methos and attributes to inheritance"""
class MyList(list):
    """This function sort the list in accendent order"""
    def print_sorted(self):
        new = self[:]
        for i in range(len(new) - 1):
            for j in range(len(new) - 1):
                if new[j] > new[j + 1]:
                    temp = new[j]
                    new[j] = new[j + 1]
                    new[j + 1] = temp
        print(new)
