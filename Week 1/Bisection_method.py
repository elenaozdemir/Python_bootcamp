import math

def f(x):
    return math.sin(x)

def find_root(a, b):
    c = (a + b)/2    # initial c
    ans = f(c)       # f(c)

    num_iterations = 0
    tolerance = 0.1

    while ans !=0 and num_iterations < 1000 and ans > tolerance:
        num_iterations += 1

        c = (a + b)/ 2
        ans = f(c)

        if (ans > 0):
            b = c
        elif (ans < 0):
            a = c

    if (num_iterations == 1000 and f(c) != 0 and ans > tolerance):
        print("There is no zero in this region with that tolerance")
        return None
    else:
        return c


lower = 3
upper = 4
print(find_root(lower, upper))
print(math.pi)