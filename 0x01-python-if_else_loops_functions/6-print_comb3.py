#!/usr/bin/python3
for number in range (100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:2d}".format(number) end=", ")
