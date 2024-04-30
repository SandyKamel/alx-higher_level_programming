#!/usr/bin/python3
def uppercase(str):
    for c in range(len(str)):
         c = chr(ord(c) - 32)
        if ord(c) >= 97 and ord(c) <= 122:
          print("{}".format(c), end="")
    print("")
