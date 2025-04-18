#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for the sixth exercise in the Python Basics course.
This script reverses a given string and prints it.
"""

def reverse_string(text):
    """
    This function takes a string as input and returns the reversed string.
    """
    return text[::-1]

def main():
    text = input("Enter a string: ")
    reversed_text = reverse_string(text)
    print(f"Reversed string: {reversed_text}")

if __name__ == "__main__":
    main()