# TODO: Write a script that prints out the common multiples of 3 and 5 between the range 0 amd N (inclusive)
#  Where N is a user input; if N is 30, the common multiples would be 0,15,30

N = int(input("Enter the upper limit: "))

for num in range(0,N+1):
    if (num % 3 == 0) and (num % 5 == 0):
        print(num)

# define f(x) = x + 1
def f(x):
    ans = x+1
    return ans #return gives you what you want the output of the functions to be, in this case you want it to return to x+1

my_soulution = f(1)
print(my_soulution)

# Example: Define a function of x, where g(x) = x^4 + x^2 +1

def g(x):
    func = x**4 + x**2 +1
    return func
solution = g(1)
print(solution)

def get_first_two_evens():   # function with multiple returns
    return 2, 4

even1, even2 = get_first_two_evens()
print(even1)
print(even2)

#funtion with no returns
def print_even(N)

    for num in range(1,N+1):
        if num % 2 == 0:
            print(num)
print_even(10)  #prints 2,4,6,8,10


# TODO: Write a function that takes N as in an input and print all common multiples of 3 and 7, between 0 and N (inclusive)

def commmon_mult(N):   #N is the upper limit
    for num in range (0,N+1):   #N+1 because we want it inclusive
        if (num % 3 == 0) and (num % 7 == 0):
            print(num)
commmon_mult(49)   #N is input to the function, not a user input

#OR you could do it with a user input

def commmon_mult():
    N = int(input("Enter your upper limit: "))
    for num in range (0,N+1):
        if (num % 3 == 0) and (num % 7 == 0):
            print(num)
commmon_mult()

# define a function that takes 3 inputs: x, y, N
# The function will find all the common multiples of x and y between 0

def find_mult(x,y,N):   # we are taking 3 inputs. problem did not state that it is a user input. it is an input to the function
    for num in range(0, N):  # did not mention inclusively
        if (num % x == 0) and (num % y == 0):
            print(num)
find_mult(3,7,100)

#OR do it with a user input

def find_mult():
    x = int(input("Enter first number:  "))
    y = int(input("Enter second number: "))
    N = int(input("Enter the upper limit: "))

    for num in range(0, N):  # did not mention inclusively
        if (num % x == 0) and (num % y == 0):
            print(num)

find_mult()

#LISTS

my_first_list = [2, 4, 6, 8]
print(my_first_list[2])   # 0 is the index value you want to access
length = len(my_first_list)
print(length)

for index in range(0, len(my_first_list)):
   element = my_first_list[index]
   print(element)

# you can use the print function instead of the for loop
# print(my_first_list)

my_first_list = [2, 4, 6, 8]
print("Original list: ", my_first_list)
my_first_list.append(10)
print("List after append:", my_first_list)

# TODO: make a list of even numbers up to 12 (inclusive)
even_list = []
for num in range(1,13):
    if num % 2 == 0:
        even_list.append(num)

print("List of even numbers up to 12", even_list)
#even_list.clear()
#print("List after using clear", even_list)

for i in range (0, len(even_list)-1):  # index has changed since the we shorthen the list
    if even_list[i] == 10:  # if element in index i is equal to 10
        index_of_ten = i
        ten = even_list.pop(i)  #pops out the element in index i when i = 10

print("the list after popping an element", even_list)
print("the value of ten = ", ten)

even_list.insert(index_of_ten, ten)
print("Using insert, to put the 10 back:", even_list)

print(sorted(even_list))  # to sort in ascending order


