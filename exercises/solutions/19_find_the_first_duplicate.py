def find_first_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("First duplicate:", find_first_duplicate(numbers))