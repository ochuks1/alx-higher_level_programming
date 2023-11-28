#!/usr/bin/python3
num1 in range(100):
    for num2 in range(num1, 100):
      print("{:02d}".format(num1), end=", " if num1 != 98 or num2 != 99 else "\n")
