#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    size = len(argv)
    add = 0
    for pos in range(1, size):
        add = add + int(argv[pos])
    print(add)
