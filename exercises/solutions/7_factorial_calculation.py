#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for the seventh exercise in the Python Basics course.
This script calculates the factorial of a given number using recursion.
"""

def factorial(n):
    """
    This function takes a non-negative integer n as input and returns its factorial.
    The factorial of n (n!) is the product of all positive integers less than or equal to n.
    It is defined as n! = n * (n-1) * (n-2) * ... * 1, and 0! is defined to be 1.
    """

    if n == 0:
        return 1
    return n * factorial(n - 1)

def main():
    """
    Main function to execute the factorial calculation.
    """
    num = int(input("Enter a number: "))
    result = factorial(num)
    print(f"The factorial of {num} is {result}.")

if __name__ == "__main__":
    main()