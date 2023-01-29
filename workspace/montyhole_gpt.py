import random

# number of doors, number of car, number of trials
num_doors = 3
num_car = 1
num_trials = 10000

# keeping track of wins and losses
switch_wins = 0
stay_wins = 0

for i in range(num_trials):
    doors = ["goat"] * (num_doors - num_car) + ["car"] * num_car
    random.shuffle(doors)

    # player chooses a door
    chosen_door = random.randint(0, num_doors-1)

    # host opens a door
    host_door = random.choice([i for i in range(num_doors) if i != chosen_door and doors[i] == "goat"])

    # player switches or stays
    switch = random.choice([True, False])
    if switch:
        final_door = [i for i in range(num_doors) if i != chosen_door and i != host_door][0]
        switch_wins += doors[final_door] == "car"
    else:
        final_door = chosen_door
        stay_wins += doors[final_door] == "car"

print("Switch wins: ", switch_wins)
print("Stay wins: ", stay_wins)
print("Switch win rate: ", switch_wins/num_trials)
print("Stay win rate: ", stay_wins/num_trials)
