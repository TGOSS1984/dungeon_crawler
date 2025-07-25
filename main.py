from utils import bold, green, red, yellow  # for text cols
from save_load import save_game, load_game
from player import Player
from dungeon import enter_dungeon
import sys

# Game intro

def print_intro():
    print(bold("=" * 40))
    print(bold("    ⚔️  Crypt of Shadows Awaits ⚔️"))
    print(bold("  A Soulbound Dungeon Crawler CLI"))
    print(bold("=" * 40))
    print(
        "\nThe air stinks of ash and regret. In the darkness, only one truth remains:\n"
        "\"All who enter must be willing to forget... or be forgotten.\"\n"
    )
    print("Choose your burden below.\n")

# Prompt player to enter name (prompt for cannot be empty)

def get_player_name():
    while True:
        name = input("Enter your character's name: ").strip()
        if name:
            return name
        else:
            print("Name cannot be empty. Try again.")

# Choose class function, print error message if not between 1–4

def choose_class():
    print("\nChoose your burden:")
    print("1. Oathbound Knight   - High vitality, heavy defence")
    print("2. Shadow Pilgrim     - Nimble and precise, but fragile")
    print("3. Ashen Scholar      - Wields forgotten flame, frail of body")
    print("4. Hollow Marksman    - Ranged attacker, cunning and swift")

    classes = {
        "1": "Oathbound Knight",
        "2": "Shadow Pilgrim",
        "3": "Ashen Scholar",
        "4": "Hollow Marksman"
    }

    while True:
        choice = input("Enter class number (1-4): ").strip()
        if choice in classes:
            return classes[choice]
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

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

        print(
            green(
                f"\nYou have chosen the path of the {player.player_class}. May the embers guide you, {player.name}."
            )
        )
        player.show_stats()

    # Connect dungeon game flow to main game loop
    input("Press Enter to step into the abyss...\n")

    result = enter_dungeon(player, room_count)

    print("\n=== Final Outcome ===")
    if result == "victory":
        print(f"🏆 {player.name}, bearer of burden — you have escaped the Crypt of Shadows.")
    elif result == "death":
        print(f"💀 {player.name} fell into darkness. The crypt claims another soul.")
    else:
        print("You fled or exited unexpectedly. The crypt waits still...")

if __name__ == "__main__":
    main()
