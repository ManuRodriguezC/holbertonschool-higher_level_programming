#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for date in dir(hidden_4):
        if date.startswith("_"):
            continue
        print(date)
