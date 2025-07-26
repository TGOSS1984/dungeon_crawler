from utils import red, green, yellow, bold  # for text cols
import random
from enemies import generate_random_enemy, Enemy
from battle import battle

# Room generation logic, max rooms 10.


def enter_dungeon(player, room_count=0):
    print(bold("\nYou descend into the Crypt of Shadows."))
    print("Ash coats the floor. The silence hums like a curse.")
    # display room count on load
    print(f"(Resuming from Room {room_count + 1})\n")

    max_rooms = 10  # After 10 rooms, trigger boss

    while player.is_alive() and room_count < max_rooms:
        input("Press Enter to tread deeper...\n")
        room_count += 1
        print(bold(f"\n🧱 Room {room_count}"))
        print("-" * 35)

        # Trigger random room generation, 5 potential options

        room_type = random.choice(
            ["enemy", "treasure", "rest", "trap", "empty"])

        if room_type == "enemy":
            enemy = generate_random_enemy()
            print(red(f"\n⚔ A {enemy.name} stirs in the shadows..."))
            result = battle(player, enemy)
            if result == "lost":
                return "death"
            elif result == "fled":
                continue

        elif room_type == "treasure":  # In treasure room random choice of 3 types 
            treasure = random.choice(["souls", "flask", "relic"])
            if treasure == "souls":
                gold_found = random.randint(10, 30) # random number between 10-30
                player.gold += gold_found
                print(
                    yellow(
                        f"You uncover scattered souls. (+{gold_found} Souls)"))
            elif treasure == "flask":
                player.potions += 1
                print(green("You found a crimson Estus Flask."))
            else:
                item = random.choice(
                    ["Withered Key", "Blighted Tome", "Tarnished Gem"])
                player.add_to_inventory(item)
                print(f"You found a relic: {item}.")

        elif room_type == "rest":
            healed = random.randint(10, 25) # random number between 10-25
            player.current_hp = min(player.current_hp + healed, player.max_hp)
            print(f"You find a cold sanctuary. (+{healed} Vitality)")

        elif room_type == "trap":
            trap_damage = random.randint(5, 15) # random number between 5-15
            player.take_damage(trap_damage)
            print(
                red(f"A forgotten rune explodes! You suffer {trap_damage} damage."))

        else:
            print("Only silence greets you. A void in space... and time.")

        player.show_stats()

        # Ask if the player wants to save
        from save_load import save_game

        save_choice = (
            input("\nWould you like to save your game? (y/n): ").strip().lower())
        if save_choice == "y":
            save_game(player, room_count)

    # Boss room
    print(bold("\n💀 The crypt yawns wide. The chamber reeks of ancient death."))
    print("A crown glints in the dark as the Undead King stirs...\n")

    boss = Enemy("Undead King")
    boss.max_hp = 100
    boss.current_hp = 100
    boss.attack = 20
    boss.defence = 8

    result = battle(player, boss)

    if result == "won":
        print(
            green(
                "\n🏆 You have shattered the Undead King's will and escaped the Crypt of Shadows!"
            )
        )
        return "victory"
    else:
        print(red("\nThe crypt claims another soul."))
        return "death"
