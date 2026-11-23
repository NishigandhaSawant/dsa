string = input("Enter a string: ")


def func(num):
    if num == 0 or num == 1:
        return num

    return func(num-1) + func(num-2)
if string.isdigit():
    print(func(int(string)))    

# tc = O(2^n) sc = O(n)