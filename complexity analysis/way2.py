#O(n) - Linear Time
def has_duplicates(numbers):
    seen = set() #empty set

    for number in numbers:
        if number in seen:
            return True

        seen.add(number)
    return False

numbers = [10, 20, 30, 40, 10]
result = has_duplicates(numbers)
if result:
    print("Duplicates found")
else:       
    print("No duplicates found")