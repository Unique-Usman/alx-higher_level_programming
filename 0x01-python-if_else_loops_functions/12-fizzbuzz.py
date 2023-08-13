#!/usr/bin/python3
def fizzbuzz():
    output = ""
    for i in range(1, 101):
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if i % 3 != 0 and i % 5 != 0:
            output += f"{str(i)}"
        if i != 100:
            output += " "
    print(output, end="")
fizzbuzz()
