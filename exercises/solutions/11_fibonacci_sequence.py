#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for the eleventh exercise in the Python Basics course.
This script generates the Fibonacci sequence up to the nth number.
"""

def fibonacci(n):
    """
    This function generates the Fibonacci sequence up to the nth number.
    The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.
    The sequence starts with 0 and 1.
    """
    sequence = [0, 1]
    for _ in range(n - 2):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def main():
    """
    Main function to execute the Fibonacci sequence generation.
    """
    n = int(input("Enter the number of terms in the Fibonacci sequence: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        fib_sequence = fibonacci(n)
        print(f"The Fibonacci sequence up to {n} terms is: {fib_sequence}")

if __name__ == "__main__":
    main()