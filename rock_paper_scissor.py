import random

# Global configuration
CHOICES = ('r', 'p', 's')
EMOJIS = {'r': '🪨', 'p': '📄', 's': '✂️'}
NAMES = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}

def get_users_choice():
    """Handles input validation logic."""
    while True:
        users_choice = input("\nMake your choice (r/p/s): ").lower().strip()
        if users_choice in CHOICES:
            return users_choice
        print("Invalid choice. Please use 'r', 'p', or 's'.")

def determine_round_winner(user, computer):
    """
    Returns: 
    1 if user wins, -1 if computer wins, 0 for tie.
    """
    if user == computer:
        return 0
    
    # Winning logic using our grouping method
    win_conditions = (
        (user == 'r' and computer == 's') or
        (user == 's' and computer == 'p') or
        (user == 'p' and computer == 'r')
    )
    
    return 1 if win_conditions else -1

def start_match():
    # --- LOGIC: Session State ---
    user_score = 0
    computer_score = 0
    history = [] # We'll store strings of each round's result here
    tie_counter = 0     # Tracks how many ties happened during the match.
    
    print("\n=== WELCOME TO THE RPS CHAMPIONSHIP ===\n")
    target_score = input("How many wins to end the match? (e.g., 2 for Best of 3): ")
    target_score = int(target_score) if target_score.isdigit() else 2

    # --- LOGIC: The Match Loop ---
    # Instead of 'while True', we loop until the players reach the target score
    while user_score < target_score and computer_score < target_score and abs(user_score - computer_score) < 2:
        print(f"\n--- Current Score: You {user_score} | Computer {computer_score} ---")
        
        u_choice = get_users_choice()
        c_choice = random.choice(CHOICES)
        
        print(f"You: {EMOJIS[u_choice]}  vs  Computer: {EMOJIS[c_choice]}")
        
        result = determine_round_winner(u_choice, c_choice)
        
        if result == 1:
            print(">> You won this round! 🎉")
            user_score += 1
            history.append(f"Round {len(history)+1}: User won ({NAMES[u_choice]} vs {NAMES[c_choice]})")
        elif result == -1:
            print(">> Computer won this round. 🤖")
            computer_score += 1
            history.append(f"Round {len(history)+1}: Computer won ({NAMES[c_choice]} vs {NAMES[u_choice]})")
        else:
            print(">> It's a tie! No points awarded.")
            history.append(f"Round {len(history)+1}: Tie ({NAMES[u_choice]})")
            tie_counter += 1

    # --- LOGIC: Final Match Summary ---
    print("\n" + "="*30)
    if user_score > computer_score:
        print("MATCH OVER: YOU ARE THE CHAMPION!")
    else:
        print("MATCH OVER: THE COMPUTER REIGNS SUPREME.")
    print("="*30)
    
    # Displaying the history list we built
    print("\nMatch History:")
    for entry in history:
        print(entry)

    # Displaying how many ties happened during the match
    if tie_counter <= 0:
        print(f"\n{tie_counter} tie happened in {len(history)} during the match.")
    else:
        print(f"\n{tie_counter} ties happened in {len(history)} rounds during the match.")

    # Asking users if they wanna play again.
    play_again = input("\nDo you want to play again? (yes/no) ").lower().strip()
    if play_again in ('no' or 'n'):
        print("Thanks for playing with me!")
    else:
        start_match()

# Executing the game
if __name__ == "__main__":
    start_match()