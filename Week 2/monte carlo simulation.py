import random

def flip_coin():
    """
    :return: a coin flip - random integer between 0 and 1
    if 1 - the coin lands on heads
    if 0 - the coin lands on tails
    """
    return random.randint(0, 1)

def monte_carlo(n):
    """
    performs a monte carlo simulation of a coin flip
    :param n: number of samples
    :return: prints out the results of the simulation
    """
    head_count = 0   #keeps track of heads & tails
    tail_count = 0
    exp_count = 0
    while exp_count < n:
        result = flip_coin()
        if result == 1:
            head_count += 1
        else:
            tail_count += 1

        exp_count += 1
    print(f"There were {n} simulations performed")
    msg = f"There were {(head_count/n) *100} % heads"
    print(msg)
    msg = f"There were {(tail_count/n)*100} % tails"
    print(msg)

monte_carlo(10000)


def roll_dice(highest_num):
    return random.randint(1,highest_num)

def monte_carlo(N):
    one_counter = 0
    two_counter = 0
    three_counter = 0
    four_counter = 0
    five_counter = 0
    six_counter = 0
    dice_max = 6

    for exp in range(0,n):
        if roll_dice(dice_max) == 1:
            one_counter += 1
        elif roll_dice(dice_max) == 1:
            two_counter += 1
        elif roll_dice(dice_max) == 1:
            three_counter += 1
        elif roll_dice(dice_max) == 1:
            four_counter += 1
        elif roll_dice(dice_max) == 1:
            five_counter += 1
        elif roll_dice(dice_max) == 1:
            six_counter += 1

    print(f"the probability of 1 = {(one_counter/N) * 100} %")
    print(f"the probability of 2 = {(two_counter / N) * 100} %")
    print(f"the probability of 3 = {(three_counter / N) * 100} %")
    print(f"the probability of 4 = {(four_counter / N) * 100} %")
    print(f"the probability of 5 = {(five_counter / N) * 100} %")
    print(f"the probability of 6 = {(six_counter / N) * 100} %")


def monte_carlo_with_lists(N, dice_max = 6):
    results = []

    for exp in range(0,N):
        results.append(roll_dice(dice_max))

    print(f"{N} experiments were performed")
    for outcome in range (1,dice_max + 1):    # 1 to 6 inclusively
        count = results.count(outcome)
        msg = f"The probability of the {outcome} = {(count/N)*100} %"
        print(msg)

dice_max = 6
print(f"The probability should converge to {(1/dice_max*100)} % ")
monte_carlo_with_lists(1000)

