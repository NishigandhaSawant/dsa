# tail recursion aka backtracking
# recursion tree 
# In tail recursion, the recursive call is the last operation in the function.
# TC - O(n) SC - O(n)

count = 0

def func():
    if count == 4:
        return
    count += 1
    func()
    print("anirudh")

func()