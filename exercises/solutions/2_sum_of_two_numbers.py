#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for the second exercise: Sum of Two Numbers.
This program takes two numbers as input from the user and prints their sum.
"""

def sum_of_two_numbers(num1, num2):
    """
    This function takes two numbers as input and returns their sum.
    
    :param num1: First number
    :param num2: Second number
    :return: Sum of num1 and num2
    """
    return num1 + num2

def main():
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    result = sum_of_two_numbers(first_number, second_number)
    print(f"The sum of {first_number} and {second_number} is: {result}")

if __name__ == "__main__":
    main()