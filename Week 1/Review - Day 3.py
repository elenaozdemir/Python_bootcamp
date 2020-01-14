# TODO: Make a function that takes in 2 inputs: An lower limit and an upper limit. The function should return a list of all multiples of 5 between
#  lower and upper limit (inclusive)

def multiples(N,M):
    mults = []
    for x in range (N,M+1):
        if x % 5 == 0:
            mults.append(x)
    return mults

print(multiples(0,100))


