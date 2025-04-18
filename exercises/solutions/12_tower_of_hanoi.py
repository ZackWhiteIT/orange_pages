def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk from {source} to {target}")
    else:
        hanoi(n - 1, source, auxiliary, target)
        hanoi(1, source, target, auxiliary)
        hanoi(n - 1, auxiliary, target, source)

hanoi(4, "A", "C", "B")