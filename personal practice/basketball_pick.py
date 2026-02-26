#this is all claude lmao i tried my best

import random

players = {
    'PG' : {'Stephen Curry' : 17, 'Magic Johnson' : 15, 'John Stockton' : 13},
    'SG' : {'Michael Jordan' : 17, 'Kobe Bryant': 15, 'Dwayne Wade' : 13},
    'SF' : {'Lebron James' : 17, 'Larry Bird': 15, 'Kevin Durant' : 13},
    'PF' : {'Dirk Nowitski' : 17, 'Tim Duncan': 15, 'Karl Malone' : 13},
    'C' : {"Shaquille O'Neal" : 17, 'Kareem Abdul-Jabaar': 15, 'Hakeem Olajuwon' : 13}
}

# Create a copy to track available positions
available_positions = list(players.keys())

# Lists to store user selections
user_team = []
total_score = 0

print("Welcome to NBA Team Builder!")
print("Each round, you'll get one random player from each remaining position.")
print("Pick one player to add to your team!\n")

# Continue until all positions are filled
while available_positions:
    print(f"\n{'='*50}")
    print(f"Positions remaining: {', '.join(available_positions)}")
    print(f"{'='*50}\n")
    
    # Generate one random player from each remaining position
    options = []
    for position in available_positions:
        # Randomly select one player from this position
        player_name = random.choice(list(players[position].keys()))
        points = players[position][player_name]
        options.append((position, player_name, points))
    
    # Display the options
    print("Available players this round:")
    for i, (pos, name, pts) in enumerate(options, 1):
        print(f"{i}. [{pos}] {name}")
    
    # Get user choice
    while True:
        try:
            choice = int(input(f"\nSelect a player (1-{len(options)}): "))
            if 1 <= choice <= len(options):
                break
            else:
                print(f"Please enter a number between 1 and {len(options)}")
        except ValueError:
            print("Please enter a valid number")
    
    # Add selected player to team
    selected_position, selected_player, points = options[choice - 1]
    user_team.append((selected_position, selected_player, points))
    total_score += points
    
    # Remove this position from available positions
    available_positions.remove(selected_position)

# Cap the score at 82
final_score = min(total_score, 82)

# Sort team by position order
position_order = ['PG', 'SG', 'SF', 'PF', 'C']
user_team_sorted = sorted(user_team, key=lambda x: position_order.index(x[0]))

# Display final team
print("\n" + "="*50)
print("YOUR FINAL TEAM:")
print("="*50)
for position, player, points in user_team_sorted:
    print(f"{position}: {player}")
print("="*50)
print(f"Total Score: {final_score}/82")
print("="*50)