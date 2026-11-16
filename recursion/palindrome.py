# check palindrome or not using recursion
# using loops

s = ["n", "i", "t", "i", "n"]

n = len(s)
left = 0
right = n - 1
while left < right:
    if s[left] != s[right]:
        print("Not a palindrome")
        break
    left += 1
    right -= 1
else:
    print("Palindrome")

