#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for the eighth exercise in the Python Basics course.
This script finds the maximum number in a list of integers provided by the user.
"""

def find_maximum(numbers):
    """
    This function takes a list of integers as input and returns the maximum number.
    """
    return max(numbers)

def main():
    """
    Main function to execute the maximum number finding.
    """
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    maximum = find_maximum(numbers)
    print(f"The maximum number is: {maximum}")

if __name__ == "__main__":
    main()