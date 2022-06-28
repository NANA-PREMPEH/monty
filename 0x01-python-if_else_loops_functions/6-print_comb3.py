#!/usr/bin/python3
for numbers in range(100):
    if int(numbers / 10) != numbers % 10 and int(numbers / 10) < numbers % 10:
        print("{}{}".format(int(numbers / 10), numbers % 10), end="")
        if (numbers != 89):
            print(", ", end="")
print("")
