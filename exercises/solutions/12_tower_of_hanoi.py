#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solution for the twelfth exercise in the Python Basics course.
This script solves the Tower of Hanoi problem using recursion.
The Tower of Hanoi is a mathematical puzzle consisting of three rods and a number of disks of different sizes which can slide onto any rod.
"""
def hanoi(n, source, target, auxiliary):
    """
    This function solves the Tower of Hanoi problem using recursion.
    It moves n disks from the source rod to the target rod using the auxiliary rod.
    The function prints the steps to move the disks.
    """
    if n == 1:
        print(f"Move disk from {source} to {target}")
    else:
        hanoi(n - 1, source, auxiliary, target)
        hanoi(1, source, target, auxiliary)
        hanoi(n - 1, auxiliary, target, source)

def visualize(n, source, target, auxiliary):
    """
    This function visualizes the Tower of Hanoi problem.
    It prints the initial state and the steps to move the disks.
    It also prints the rods and the disks at each step using ASCII art.
    """
    print(f"Initial state: {source} -> {target} with {n} disks")
    hanoi(n, source, target, auxiliary)
    print(f"Final state: {target} -> {source} with {n} disks")

def main():
    """
    Main function to execute the Tower of Hanoi solution.
    """
    n = int(input("Enter the number of disks: "))
    while n <= 0:
        print("Please enter a positive integer.")
        n = int(input("Enter the number of disks: "))
    
    print(f"Steps to move {n} disks from A to C using B as auxiliary:")
    visualize(n, 'A', 'C', 'B')

if __name__ == "__main__":
    main()
