#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    size = len(argv)
    total = 0
    for add in range(1, size):
        total = total + int(argv[add])
    print(total)
