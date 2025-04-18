#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for the fourth exercise: Even or Odd.
This program checks if a number is even or odd.
"""

def even_or_odd(number):
    """
    Check if a number is even or odd.
    :param number: The number to check
    :return: "even" if the number is even, "odd" if the number is odd
    """
    if number % 2 == 0:
        return("even")
    else:
        return("odd")

def main():
    num = int(input("Enter a number: "))
    result = even_or_odd(num)
    print(f"The number {num} is: {result}")

if __name__ == "__main__":
    main()