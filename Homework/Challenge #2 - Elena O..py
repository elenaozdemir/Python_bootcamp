# challenge #2:
def find_min(list):
    if len(list) == 0:
        return None

    current_min = list[0]
    for i in range(0,len(list)):
        if list[i] <= current_min:
            current_min = list[i]
    return current_min

my_list = [2.5,6.2,3.14]
ans = find_min(my_list)
print(ans)