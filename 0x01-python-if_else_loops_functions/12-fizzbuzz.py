#!/usr/bin/python3
def fizzbuzz():
    for nmber in range(1, 101):
        if nmber % 3 == 0 and nmber % 5 == 0:
            print("FizzBuzz ", end="")
        elif nmber % 5 == 0:
            print("Buzz ", end="")
        elif nmber % 3 == 0:
            print("Fizz ", end="")
        else:
            print(f"{nmber} ", end="")
