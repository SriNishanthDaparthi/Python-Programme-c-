# Find second largest number
lst = list(map(int, input("Enter numbers: ").split()))

largest = second = float('-inf')

for num in lst:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest:", second)
