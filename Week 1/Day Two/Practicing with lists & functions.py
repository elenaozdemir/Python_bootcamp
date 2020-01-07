# practicing with lists and functions

# EXAMPLE: Define a function that returns a list of even numbers
# between A and B (inclusive)

def find_events(A,B):
    # make an empty list to return to something
    evens = []
    for nums in range (A,B+1):   #inclusive
        if (nums % 2 == 0):
        evens.append(nums)
    return evens

print(find_events(2,20))

# TODO: Define a function that returns a list of numbers between A and B (inclusive) that are multiples of 3

def list_num(A,B):
    numlist = []
    for numbers in range (A,B+1):
        if (numbers % 2 == 0) and (numbers % 3 == 0):    # or you can just do (numbers % 6 == 0), even multiples of 2 and 3
            numlist.append(numbers)
    return numlist

print(list_num(3,20))


