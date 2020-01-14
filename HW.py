#Problem 3:
def find_odds(n):
    odds = []
    for num in range (0, n+1):
        if (num % 2 == 1):
            odds.append(num)
    return odds

n = 19
print(find_odds(n))

#Problem 4: finding the differences between two lists without the use of sets

def find_diffs(a,b):
    differences = []
    for element in a:
        if element not in b:
            differences.append(element)

    for element in b:
        if element not in a:
            differences.append(element)

    return differences

test1 = [1,2,3]
test2 = [1,2,3]

print(find_diffs(test1, test2))

