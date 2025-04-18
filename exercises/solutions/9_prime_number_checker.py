#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for the ninth exercise in the Python Basics course.
This script checks if a given number is prime or not.
"""

def is_prime(num):
    """
    This function checks if a number is prime.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    """
    Main function to execute the prime number checking.
    """
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

if __name__ == "__main__":
    main()