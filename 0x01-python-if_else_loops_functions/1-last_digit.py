#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lst_digit = number % 10 if number >= 0 else ((-number % 10) * -1)
message = f"Last digit of {number} is {lst_digit}"

if lst_digit == 0:
    print(f"{message} and is 0")
elif lst_digit > 5 and lst_digit % 10 != 0:
    print(f"{message} and is greater than 5")
else:
    print(f"{message} and is less than 6 and not 0")
