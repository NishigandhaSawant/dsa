# print "anirudh" 4 times using recursion
# head recursion
# In head recursion, the recursive call is the first operation in the function.
# TC - O(n) SC - O(n)
def func(count=0):
    if count == 4:
        return
    print("anirudh")
    func(count + 1)

func()