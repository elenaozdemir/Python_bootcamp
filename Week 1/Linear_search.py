# TODO: Write a function that takes an integer and a list as the input. The function should return the index of where the integer was found on the list

def LinearSearch(x, list):
    """
    this function returns the index of where the element x was found
    on the list
    """
    for index in range(0,len(list)):
        if list[index] == x:
            return index

my_list = [10, 8, 7, 19, 42, 20]
ans = LinearSearch(20, my_list)
print(ans)

def find_max(list):
    """
    this function returns the maximum element in the list
    :param list: a list of numerical elements
    :return: the maximum value in the list
    """
    current_max = list[0]

    for index in range(0,len(list)):
     # since we don't need the indexes in this case, we can just use
     # for element in list:
     #    if element >= max:
     #     max = element

        if list[index] >= current_max:
            current_max = list[index]
    return current_max

my_list = [10, 8, 19, 42, 17, 20]
ans = find_max(my_list)
print(ans)

