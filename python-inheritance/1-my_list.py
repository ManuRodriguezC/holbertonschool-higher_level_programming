#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        new = self[:]
        for i in range(len(new) - 1):
            for j in range(len(new) - 1):
                if new[j] > new[j + 1]:
                    temp = new[j]
                    new[j] = new[j + 1]
                    new[j + 1] = temp
        print(new)
