# tc = O(n) sc = O(n)
palindrome_str = input("Enter a string: ")

def func(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return func(s, left + 1, right - 1)

print(func(palindrome_str, 0, len(palindrome_str) - 1))