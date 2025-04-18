balance = 1000
amount = int(input("Enter withdrawal amount: "))
if amount <= balance:
    balance -= amount
    print(f"Withdrawal successful. Remaining balance: {balance}")
else:
    print("Insufficient funds.")