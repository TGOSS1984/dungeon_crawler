from player import Player
import sys

# Game intro

def print_intro():
    print("=" * 40)
    print("  Welcome to the Crypt of Shadows")
    print("      A Dungeon Crawler CLI Game")
    print("=" * 40)
    print("\nYou must choose your class to begin.\n")

# Prompt player to enter name (prompt for cannot be empty)   

def get_player_name():
    while True:
        name = input("Enter your character's name: ").strip()
        if name:
            return name
        else:
            print("Name cannot be empty. Try again.")

# Choose class function, print error message if not between 1&3

def choose_class():
    print("\nChoose your class:")
    print("1. Warrior - High HP & defence")
    print("2. Rogue   - Balanced & agile")
    print("3. Mage    - High attack, low defence")

    classes = {"1": "Warrior", "2": "Rogue", "3": "Mage"}

    while True:
        choice = input("Enter class number (1-3): ").strip()
        if choice in classes:
            return classes[choice]
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def main():
    print_intro()
    name = get_player_name()
    player_class = choose_class()
    
    try:
        player = Player(name, player_class)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    print(f"\nYou have chosen the path of the {player_class}. Good luck, {name}!")
    player.show_stats()

    # Connect dungeon game flow to main game loop
    input("Press Enter to enter the dungeon...\n")

    result = enter_dungeon(player)

    print("\n=== Final Outcome ===")
    if result == "victory":
        print(f"🏆 Congratulations {player.name}, you survived the Crypt of Shadows!")
    elif result == "death":
        print(f"💀 {player.name} perished in the crypt. Your journey ends here.")
    else:
        print("You fled or exited unexpectedly.")

if __name__ == "__main__":
    main()