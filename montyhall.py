import random  # Import the random library for shuffling and random choices

# Function to set up doors and choose a door for the prize
def setup_game():
    doors = ["goat", "goat", "car"]  
    random.shuffle(doors)  
    return doors





# Function for player's choice and host revealing a goat door
def player_and_host(doors):
    pass






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