#matplotlib
import matplotlib.pyplot as pilot
import random

def roll_dice():
    dice_1 = random.randint(1, 8)
    dice_2 = random.randint(1, 8)
    if(dice_1==dice_2):
        same_num = True
    else:
        same_num = False
    return same_num

simulations = 666
dice_rolls = 222
placed_bet = 1
winning = []
balance = []
pilot.title('Numbers [' + str(simulations) + ']')
pilot.xlabel('RollNumber')
pilot.ylabel('Money[R]')
pilot.xlim([0, dice_rolls])
for i in range(simulations):
    tbalance = [1000]
    rolles = [0]
    wins = 0
    while(rolles[-1]<dice_rolls):
        same = roll_dice()
        if(same):
            tbalance.append(tbalance[-1] + 4 * placed_bet)
            wins += 1
        else:
            tbalance.append(tbalance[-1] - placed_bet)
        rolles.append(rolles[-1] + 1)
    winning.append(wins/rolles[-1])
    balance.append(tbalance[-1])
    pilot.plot(rolles, tbalance)
pilot.show()
winrate = sum(winning)/len(winning)
endrate = sum(balance)/len(balance)
print(str(simulations) + 'runs: ' + str(winrate))
print(str(simulations) + 'runs: R' + str(endrate))