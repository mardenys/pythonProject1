import random

def throw_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2

def roll_result(dice1, dice2):
    sum_dice = dice1 + dice2
    if sum_dice <= 6:
        return f"The sum of your dice is {sum_dice}. Unfortunate"
    elif sum_dice > 6 and sum_dice < 10:
        return f"The sum of your dice is {sum_dice}. You have a good chance"
    else:
        return f"The sum of your dice is {sum_dice}. It looks like a winning roll"

dice1, dice2 = throw_dice()
result = roll_result(dice1, dice2)
print(result)