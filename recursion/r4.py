"""print 1 to N using recursion"""

def func(i,n):
    if i>n:
        return
    print(i)
    func(i+1,n)
func(1,5)


"""backtracking (tail recursion)"""

def func(i,n):
    if i>n:
        return
    func(i+1,n)
    print(i)
func(1,5)