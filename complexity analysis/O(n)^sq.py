def find_duplicates(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i!=j and numbers[i] == numbers[j]:
                return True
    return False

numbers = [1, 2, 3, 2, 4, 5, 6, 7, 8, 9, 10]
result = find_duplicates(numbers)   

if result:
    print("Duplicates found")
else:
    print("No duplicates found")