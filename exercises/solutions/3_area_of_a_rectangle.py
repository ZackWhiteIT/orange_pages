#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for the third exercise: Calculate the area of a rectangle.
This program takes the length and width of a rectangle as input from the user and prints its area.
"""

def area(length, width):
    """
    Calculate the area of a rectangle.
    :param length: Length of the rectangle
    :param width: Width of the rectangle
    :return: Area of the rectangle
    """
    return length * width

def main():
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    result = area(first_number, second_number)
    print(f"The area of {first_number} and {second_number} is: {result}")

if __name__ == "__main__":
    main()