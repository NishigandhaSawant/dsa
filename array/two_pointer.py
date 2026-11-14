def find_two_numbers(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return (numbers[left], numbers[right])
        elif total < target:
            left += 1
        else:
            right -= 1

    return []

numbers = [ 1, 3, 5, 8, 11]
print(find_two_numbers(numbers, 9))  # Output: (1, 8)
print(find_two_numbers(numbers, 15))  # Output: (4, 11)