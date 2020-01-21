# challenge #1
def find_max(list):

    if len(list) == 0:
        return None

    current_max = list[0]
    for index in range(0, len(list)):

        if list[index] >= current_max:
            current_max = list[index]
    return current_max

my_list = [1,2,3]
ans = find_max(my_list)
print(ans)
