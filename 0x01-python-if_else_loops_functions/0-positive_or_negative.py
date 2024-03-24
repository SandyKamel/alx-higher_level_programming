#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0 :
    print("{} your number is positive". format(number))
elif number == 0 :
    print ("{} your number is zero" . format(number))
else :
print ("{} your number is negative" . format(number))
