# Exercises

The beginner-friendly puzzles below will help students build foundational programming skills while keeping things fun and practical. Each challenge is solvable within **10 minutes**.

## 🏆 Python Coding Challenge Leaderboard  

Earn points by solving puzzles and level up your coding skills. The goal is to reach **100 points** by completing challenges.  

- 🟢 **Beginner Level (0-30 Points)** → Introductory problems (1-3 points each)  
- 🔵 **Intermediate Level (31-70 Points)** → More complex logic and problem-solving (4-6 points each)  
- 🔴 **Advanced Level (71-100 Points)** → Challenging puzzles requiring deeper thinking (7-10 points each)  

### 🟢 **Beginner Level: Getting Started (1-3 Points Each)**  

| 🏆 Challenge | Concepts | Points |
|-------------|---------|--------|
| 1️⃣ Hello, World! | Printing output | 1️⃣ |
| 2️⃣ Sum of Two Numbers | Variables & Arithmetic | 2️⃣ |
| 3️⃣ Area of a Rectangle | User input & multiplication | 3️⃣ |
| 4️⃣ Even or Odd? | Conditional statements | 3️⃣ |
| 5️⃣ The FizzBuzz Challenge | Loops & conditionals | 3️⃣ |
| 6️⃣ Reverse a String | String slicing | 3️⃣ |
| 7️⃣ Factorial Calculation | Recursion | 3️⃣ |

### 🔵 **Intermediate Level: Logic & Problem-Solving (4-6 Points Each)**  

| 🏆 Challenge | Concepts | Points |
|-------------|---------|--------|
| 8️⃣ Find the Maximum in a List | Lists & functions | 4️⃣ |
| 9️⃣ Prime Number Checker | Loops & divisibility | 4️⃣ |
| 🔟 Guess the Number Game | Random numbers & conditionals | 4️⃣ |
| 1️⃣1️⃣ Fibonacci Sequence | Loops & sequences | 5️⃣ |
| 1️⃣2️⃣ Tower of Hanoi | Recursion & problem-solving | 5️⃣ |
| 1️⃣3️⃣ Celsius to Fahrenheit Converter | Mathematical formulas | 4️⃣ |
| 1️⃣4️⃣ Counting Vowels | String processing | 5️⃣ |
| 1️⃣5️⃣ Palindrome Checker | String manipulation | 5️⃣ |
| 1️⃣6️⃣ Rock, Paper, Scissors | Conditional logic | 5️⃣ |
| 1️⃣7️⃣ Bubble Sort Algorithm | Sorting algorithms | 6️⃣ |

### 🔴 **Advanced Level: Strategic Thinking & Algorithms (7-10 Points Each)**  

| 🏆 Challenge | Concepts | Points |
|-------------|---------|--------|
| 1️⃣8️⃣ Tic-Tac-Toe Game | Multi-dimensional lists & logic | 7️⃣ |
| 1️⃣9️⃣ Find the First Duplicate | Lists & sets | 7️⃣ |
| 2️⃣0️⃣ ATM Withdrawal Simulator | Conditional statements | 7️⃣ |
| 2️⃣1️⃣ Remove Duplicates from a List | List & set operations | 7️⃣ |
| 2️⃣2️⃣ Password Strength Checker | Regular expressions & conditionals | 8️⃣ |
| 2️⃣3️⃣ Hangman Game | String manipulation & loops | 8️⃣ |
| 2️⃣4️⃣ Simple Encryption (Caesar Cipher) | Encoding & decoding | 8️⃣ |
| 2️⃣5️⃣ Anagram Checker | Sorting & string comparison | 9️⃣ |
| 2️⃣6️⃣ GCD Finder | Math & recursion | 9️⃣ |
| 2️⃣7️⃣ Word Frequency Counter | Data structures (dictionaries) | 9️⃣ |
| 2️⃣8️⃣ Collatz Conjecture | Sequences & loops | 9️⃣ |
| 2️⃣9️⃣ Binary Search Algorithm | Efficient searching | 🔟 |
| 3️⃣0️⃣ Conway’s Game of Life | Cellular automata | 🔟 |

### 🏅 **How to Play**

1️⃣ Start with the **Beginner Level** challenges to earn **0-30 points**.  
2️⃣ Move on to **Intermediate Level** challenges as you reach **31-70 points**.  
3️⃣ Conquer the **Advanced Level** to reach **100 points and beyond**!  
4️⃣ Track your progress and challenge teammates to a friendly competition.  

## 🟢 **Beginner Level (1-3 Points Each)**

**Goal:** Build a strong foundation in Python basics.  

### **1️⃣ Hello, World!** (1 Point)  

Print `"Hello, World!"` to the screen.  

```python
print("Hello, World!")
```

### **2️⃣ Sum of Two Numbers** (2 Points)  

Write a program that adds two numbers and prints the result.  

```python
a = 5
b = 7
print(a + b)
```

### **3️⃣ Area of a Rectangle** (3 Points)  

Prompt the user for the width and height of a rectangle, then calculate and print its area.  

```python
width = float(input("Enter width: "))
height = float(input("Enter height: "))
print("Area:", width * height)
```

### **4️⃣ Even or Odd?** (3 Points)  

Write a program that checks whether a number is even or odd.  

```python
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### **5️⃣ The FizzBuzz Challenge** (3 Points)  

Print numbers from 1 to 20. If the number is divisible by 3, print `"Fizz"`, if divisible by 5 print `"Buzz"`, and if both, print `"FizzBuzz"`.  

```python
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

### **6️⃣ Reverse a String** (3 Points)  

Take an input string and reverse it.  

```python
text = input("Enter text: ")
print(text[::-1])
```

### **7️⃣ Factorial Calculation** (3 Points)  

Write a function to compute the factorial of a given number.  

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number: "))
print(factorial(num))
```

---

## 🔵 **Intermediate Level (4-6 Points Each)**

**Goal:** Strengthen problem-solving skills and introduce algorithmic thinking.  

### **8️⃣ Find the Maximum in a List** (4 Points)  

Ask the user for a list of numbers and find the maximum.  

```python
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Max:", max(numbers))
```

### **9️⃣ Prime Number Checker** (4 Points)  

Check if a number is prime.  

```python
num = int(input("Enter a number: "))
if num < 2:
    print("Not prime")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")
```

### **🔟 Guess the Number Game** (4 Points)  

Let the user guess a randomly generated number between 1 and 10.  

```python
import random

number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("Correct!")
else:
    print(f"Wrong! The number was {number}.")
```

### **1️⃣1️⃣ Fibonacci Sequence** (5 Points)  

Generate the first 10 numbers in the Fibonacci sequence.  

```python
def fibonacci(n):
    sequence = [0, 1]
    for _ in range(n - 2):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

print(fibonacci(10))
```

### **1️⃣2️⃣ Tower of Hanoi** (5 Points)  

Solve the Tower of Hanoi problem with three rods and four disks.  

```python
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk from {source} to {target}")
    else:
        hanoi(n - 1, source, auxiliary, target)
        hanoi(1, source, target, auxiliary)
        hanoi(n - 1, auxiliary, target, source)

hanoi(4, "A", "C", "B")
```

### **1️⃣3️⃣ Celsius to Fahrenheit Converter** (4 Points)  

Write a program that converts Celsius to Fahrenheit.

```python
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is {fahrenheit}°F")
```

### **1️⃣4️⃣ Counting Vowels** (5 Points)  

Write a function that counts the number of vowels in a given string.

```python
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

text = input("Enter text: ")
print(f"Vowel count: {count_vowels(text)}")
```

### **1️⃣5️⃣ Palindrome Checker** (5 Points)  

Check if a word or phrase is a palindrome.

```python
text = input("Enter text: ").replace(" ", "").lower()
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
```

### **1️⃣6️⃣ Rock, Paper, Scissors Game** (5 Points)  

Create a simple **Rock-Paper-Scissors** game against the computer.

```python
import random

choices = ["rock", "paper", "scissors"]
user = input("Choose rock, paper, or scissors: ").lower()
computer = random.choice(choices)

print(f"Computer chose {computer}")
if user == computer:
    print("It's a tie!")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("You lose!")
```

### **1️⃣7️⃣ Bubble Sort Algorithm** (6 Points)  

Implement the **Bubble Sort** algorithm to sort a list of numbers.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Sorted:", bubble_sort(numbers))
```

## 🔴 **Advanced-Level Puzzles (7-10 Points Each)**  

**Goal:** Master complex logic, algorithms, and deep problem-solving skills.

### **1️⃣8️⃣ Tic-Tac-Toe Game** (7 Points)  

Create a **text-based Tic-Tac-Toe** game where two players take turns.

```python
def print_board(board):
    for row in board:
        print(" | ".join(row))
    print()

def check_winner(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] != " ":
        return board[1][1]
    return None

board = [[" "]*3 for _ in range(3)]
player = "X"

for _ in range(9):
    print_board(board)
    row, col = map(int, input(f"Player {player}, enter row and column (0-2): ").split())
    if board[row][col] == " ":
        board[row][col] = player
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        player = "O" if player == "X" else "X"
    else:
        print("Invalid move, try again!")
else:
    print("It's a tie!")
```

---

### **1️⃣9️⃣ Find the First Duplicate** (7 Points)  

Write a function to find the **first duplicate** number in a list.

```python
def first_duplicate(numbers):
    seen = set()
    for num in numbers:
        if num in seen:
            return num
        seen.add(num)
    return None

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("First duplicate:", first_duplicate(numbers))
```

---

### **2️⃣0️⃣ ATM Withdrawal Simulator** (7 Points)  

Simulate an **ATM withdrawal** by checking balance before deducting an amount.

```python
balance = 1000  # Assume the user has $1000 in their account
amount = float(input("Enter withdrawal amount: "))

if amount > balance:
    print("Insufficient funds!")
else:
    balance -= amount
    print(f"Withdrawal successful! New balance: ${balance:.2f}")
```

---

### **2️⃣1️⃣ Remove Duplicates from a List** (7 Points)  

Remove **duplicate numbers** from a list and return a sorted version.

```python
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
unique_numbers = sorted(set(numbers))
print("Unique numbers:", unique_numbers)
```

---

### **2️⃣2️⃣ Password Strength Checker** (8 Points)  

Check **password strength** based on length and character variety.

```python
import re

password = input("Enter a password: ")

length_score = len(password) >= 8
uppercase_score = bool(re.search(r'[A-Z]', password))
lowercase_score = bool(re.search(r'[a-z]', password))
digit_score = bool(re.search(r'[0-9]', password))
special_score = bool(re.search(r'[\W_]', password))

score = sum([length_score, uppercase_score, lowercase_score, digit_score, special_score])

if score == 5:
    print("Strong password!")
elif score >= 3:
    print("Moderate password.")
else:
    print("Weak password, consider making it stronger.")
```

---

### **2️⃣3️⃣ Hangman Game** (8 Points)  

Create a **word-guessing Hangman game**.

```python
import random

words = ["python", "computer", "programming", "developer", "algorithm"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

while attempts > 0 and "_" in guessed:
    print(" ".join(guessed))
    letter = input("Guess a letter: ").lower()

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
    else:
        attempts -= 1
        print(f"Wrong guess! Attempts left: {attempts}")

if "_" not in guessed:
    print(f"Congrats! The word was '{word}'.")
else:
    print(f"Game over! The word was '{word}'.")
```

### **2️⃣4️⃣ Simple Encryption (Caesar Cipher)** (8 Points)  

Implement a **Caesar Cipher** for encoding and decoding messages.

```python
def caesar_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr(shift_base + (ord(char) - shift_base + shift) % 26)
        else:
            result += char
    return result

message = input("Enter a message: ")
shift = int(input("Enter shift value: "))
encrypted = caesar_cipher(message, shift)
print("Encrypted:", encrypted)
print("Decrypted:", caesar_cipher(encrypted, shift, decrypt=True))
```

---

### **2️⃣5️⃣ Anagram Checker** (9 Points)  

Check if **two words are anagrams**.

```python
def is_anagram(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())

word1 = input("Enter first word: ")
word2 = input("Enter second word: ")
print("Anagram!" if is_anagram(word1, word2) else "Not an anagram.")
```

---

### **2️⃣6️⃣ GCD Finder (Greatest Common Divisor)** (9 Points)  

Find the **GCD** of two numbers using the **Euclidean algorithm**.

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("GCD:", gcd(num1, num2))
```

---

### **2️⃣7️⃣ Word Frequency Counter** (9 Points)  

Analyze a block of **text** and count word occurrences.

```python
from collections import Counter

text = input("Enter text: ").lower().split()
word_counts = Counter(text)
print(word_counts)
```

---

### **2️⃣8️⃣ Collatz Conjecture Simulator** (9 Points)  

Simulate the **Collatz Conjecture** sequence.

```python
def collatz(n):
    while n != 1:
        print(n, end=" → ")
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    print(1)

num = int(input("Enter a number: "))
collatz(num)
```

---

### **2️⃣9️⃣ Binary Search Algorithm** (10 Points)  

Efficiently **search for a number** in a sorted list.

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

numbers = sorted(map(int, input("Enter sorted numbers separated by spaces: ").split()))
target = int(input("Enter number to find: "))
index = binary_search(numbers, target)
print(f"Found at index {index}" if index != -1 else "Not found.")
```

---

### **3️⃣0️⃣ Conway’s Game of Life** (10 Points)  

Simulate **Conway’s Game of Life**, a cellular automaton.

```python
import random

rows, cols = 10, 10
grid = [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

def print_grid(grid):
    for row in grid:
        print(" ".join("⬛" if cell else "⬜" for cell in row))
    print()

def next_generation(grid):
    new_grid = [[0]*cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            neighbors = sum(grid[i][j] for i in range(max(0, r-1), min(rows, r+2))
                            for j in range(max(0, c-1), min(cols, c+2)) if (i, j) != (r, c))
            new_grid[r][c] = 1 if (grid[r][c] and 2 <= neighbors <= 3) or (not grid[r][c] and neighbors == 3) else 0
    return new_grid

for _ in range(5):  # Run for 5 generations
    print_grid(grid)
    grid = next_generation(grid)
```
