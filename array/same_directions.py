def clean(names):
    left = 0
    for right in range(1, len(names)):
        if names[right] != names[left]:
            left += 1
            names[left] = names[right]
    return left + 1

names = ["Alice", "Bob", "Bob", "Charlie", "Charlie", "David"]
count = clean(names)
print(names[:count])  # Output: ['Alice', 'Bob', 'Charlie', 'David']