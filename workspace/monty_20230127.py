import random

def monty_hall(num_doors, num_correct, num_trials):
    switch_wins = 0
    stay_wins = 0
    
    for i in range(num_trials):
        doors = [0] * num_doors
        correct_door = random.randint(0, num_doors-1)
        doors[correct_door] = 1
        
        # Player chooses a door
        player_choice = random.randint(0, num_doors-1)
        
        # Monty opens all but the correct door and the door chosen by the player
        opened_doors = []
        for j in range(num_doors):
            if j != correct_door and j != player_choice:
                opened_doors.append(j)
        
        # Monty randomly opens one of the remaining doors
        monty_choice = random.choice(opened_doors)
        
        # The player switches to the remaining door
        switch_choice = [i for i in range(num_doors) if i not in (player_choice, monty_choice)][0]
        
        if switch_choice == correct_door:
            switch_wins += 1
        elif player_choice == correct_door:
            stay_wins += 1
    
    switch_win_percent = switch_wins / num_trials * 100
    stay_win_percent = stay_wins / num_trials * 100
    
    return switch_win_percent, stay_win_percent

# Example usage
num_doors = 3
num_correct = 1
num_trials = 10000
switch_win_percent, stay_win_percent = monty_hall(num_doors, num_correct, num_trials)
print(f"Switching wins {switch_win_percent}% of the time.")
print(f"Staying wins {stay_win_percent}% of the time.")
