def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

numbers = sorted(list(map(int, input("Enter sorted numbers separated by spaces: ").split())))
target = int(input("Enter target number: "))
result = binary_search(numbers, target)
print("Index:", result if result != -1 else "Not found")