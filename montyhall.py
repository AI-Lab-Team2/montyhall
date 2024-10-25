import random  # Import the random library for shuffling and random choices

# Function to set up doors and choose a door for the prize
def setup_game():
    pass





# Function for player's choice and host revealing a goat door
def player_and_host(doors):
    player_choice = random.randint(0, 2) # Player picks a random door

    # Host opens a door with a goat (not chosen by the player)
    host_choice = next(i for i in range(3) if i != player_choice and doors[i] != "car")
    return player_choice, host_choice





# Function to switch choice and check if player wins
def check_win(doors, player_choice, host_choice, switch):
    pass





# Main function to run simulations and print win rates
def run_simulation(num_games, switch):
    pass






# Run simulations
if __name__ == "__main__":
    run_simulation(1000, switch=True)  # Simulate with switching
    run_simulation(1000, switch=False)  # Simulate without switching
