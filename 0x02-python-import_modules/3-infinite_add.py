#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    outcome = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            outcome += int(arg)
    print(outcome)
