# challenge #5:
def min_max_values(new_list):
    sum_ = 0
    for index in range(0,len(new_list)):
        sum_ += new_list[index]

        current_max = new_list[0]

        if new_list[index] >= current_max:
            current_max = new_list[index]

        current_min = new_list[0]

        if new_list[index] <= current_min:
            current_min = new_list[index]
    print(sum_ - current_max)
    print(sum_ - current_min)

list = [2,4,6,8,10]
min_max_values(list)