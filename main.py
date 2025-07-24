from utils import bold, green, red, yellow # for text cols
from save_load import save_game, load_game
from player import Player
from dungeon import enter_dungeon
import sys

# Game intro

def print_intro():
    print(bold("=" * 40))
    print(bold("  Welcome to the Crypt of Shadows"))
    print(bold("      A Dungeon Crawler CLI Game"))
    print(bold("=" * 40))
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
    # Save/Load function
    choice = input("Do you want to load a saved game? (y/n): ").strip().lower()
    player = None
    room_count = 0

    if choice == "y":
        player, room_count = load_game()
        if not player:
            print("\nNo save found or failed to load. Starting new game...\n")
            player = None
            room_count = 0


    if not player:
        name = get_player_name()
        player_class = choose_class()
        try:
            player = Player(name, player_class)
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)

        print(green(f"\nYou have chosen the path of the {player.player_class}. Good luck, {player.name}!"))
        player.show_stats()

    # Connect dungeon game flow to main game loop
    input("Press Enter to enter the dungeon...\n")

    result = enter_dungeon(player, room_count)

    print("\n=== Final Outcome ===")
    if result == "victory":
        print(f"🏆 Congratulations {player.name}, you survived the Crypt of Shadows!")
    elif result == "death":
        print(f"💀 {player.name} perished in the crypt. Your journey ends here.")
    else:
        print("You fled or exited unexpectedly.")

if __name__ == "__main__":
    main()