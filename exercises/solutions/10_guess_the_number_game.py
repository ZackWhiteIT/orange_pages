#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for the tenth exercise in the Python Basics course.
This script implements a simple number guessing game.
"""

import random

def guess_the_number():
    """
    This function implements a simple number guessing game.
    The user has to guess a number between 1 and 10.
    """
    number = random.randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == number:
        return("Correct!")
    else:
        return(f"Wrong! The number was {number}.")

def main():
    """
    Main function to execute the number guessing game.
    """
    result = guess_the_number()
    print(result)

if __name__ == "__main__":
    main()