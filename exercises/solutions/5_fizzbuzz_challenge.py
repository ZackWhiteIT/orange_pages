#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for the fifth exercise in the Python Basics course.
This script checks if a number is even or odd and prints the numbers from 1 to 20 with FizzBuzz rules.
"""

def fizz_buzz(number):
    """
    This function takes a number as input and prints "Fizz" for multiples of 3,
    "Buzz" for multiples of 5, and "FizzBuzz" for multiples of both 3 and 5.
    It prints the numbers from 1 to the given number.
    """
    for i in range(1, number):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i}: FizzBuzz")
        elif i % 3 == 0:
            print(f"{i}: Fizz")
        elif i % 5 == 0:
            print(f"{i}: Buzz")
        else:
            print(i)

def main():
    num = int(input("Enter a number: "))
    fizz_buzz(num)

if __name__ == "__main__":
    main()