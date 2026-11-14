# recursion using parameters
# print x 4 times using recursion
# tc - O(n) sc - O(n)

def func(x, N):
    if N == 0:
        return
    print(x)
    func(x, N - 1)

func(15, 4)