#!/usr/bin/env python

num1 = int(input("Enter a Number: \n"))
num2 = int(input("Enter a second Number: \n"))

try:
    print(num1//num2)
except ZeroDivisionError:
    print("Dividing by zero is not allowed")
