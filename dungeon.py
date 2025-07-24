import random
from enemies import generate_random_enemy, Enemy
from battle import battle

# Room generation logic, max rooms 10.

def enter_dungeon(player):
    print("\nYou step into the crypt. Shadows dance along the walls...\n")
    room_count = 0
    max_rooms = 10  # After 10 rooms, trigger boss

    while player.is_alive() and room_count < max_rooms:
        input("Press Enter to proceed to the next room...\n")
        room_count += 1
        print(f"\n🧱 Room {room_count}\n" + "-" * 30)

        # Random result of what might be found in a room with logic for each result

        room_type = random.choice(["enemy", "treasure", "rest", "trap", "empty"])

        if room_type == "enemy":
            enemy = generate_random_enemy()
            result = battle(player, enemy)
            if result == "lost":
                return "death"
            elif result == "fled":
                continue
        elif room_type == "treasure":
            treasure = random.choice(["gold", "potion", "mysterious item"])
            if treasure == "gold":
                gold_found = random.randint(10, 30)
                player.gold += gold_found
                print(f"You find a pile of gold! (+{gold_found} gold)")
            elif treasure == "potion":
                player.potions += 1
                print("You found a healing potion!")
            else:
                item = random.choice(["Rusty Key", "Ancient Scroll", "Gemstone"])
                player.add_to_inventory(item)
                print(f"You found a {item}!")
        elif room_type == "rest":
            healed = random.randint(10, 25)
            player.current_hp = min(player.current_hp + healed, player.max_hp)
            print(f"You find a quiet corner to rest. (+{healed} HP)")
        elif room_type == "trap":
            trap_damage = random.randint(5, 15)
            player.take_damage(trap_damage)
            print(f"A trap triggers! You take {trap_damage} damage.")
        else:
            print("The room is eerily silent. Nothing happens...")

        player.show_stats()

    # Boss room
    print("\n💀 You enter a vast chamber... the final boss awaits!\n")
    boss = Enemy("Undead King")
    boss.max_hp = 100
    boss.current_hp = 100
    boss.attack = 20
    boss.defense = 8

    result = battle(player, boss)

    if result == "won":
        print("\n🏆 You have defeated the Undead King and escaped the crypt!")
        return "victory"
    else:
        print("\nThe darkness consumes you...")
        return "death"