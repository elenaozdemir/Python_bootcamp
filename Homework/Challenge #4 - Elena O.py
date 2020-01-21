# challenge #4:
def odd_numbers(numbers):
    new_list = []
    for i in numbers:
        if i % 2 == 1:
            new_list.append(i)
    if not len(new_list) == 0:       # proceed if all numbers in the new_list are odd
        current_max = new_list[0]
        for nums in range(0, len(new_list)):
            if new_list[nums] >= current_max:
                current_max = new_list[nums]

        current_min = new_list[0]
        for nums in range(0, len(new_list)):
            if new_list[nums] <= current_min:
                current_min = new_list[nums]
        if current_min == current_max:
            add = current_max + current_min
            print(add)
        else:
            sum_1 = current_max + current_min
            print(sum_1)
    else:                 # for the case of even numbers
        return 0

# or could use print(min(new_list) + max(new_list)) to find sum

l = [2,4,6,8,10,3]
odd_numbers(l)




