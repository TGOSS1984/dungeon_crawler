from enemies import Enemy
from player import Player
import random
import time

# Enemy appears note with logic for turn based battle, pick from 3 options

def battle(player, enemy):
    print("\n⚔️ A wild", enemy.name, "appears!")
    enemy.show_stats()

    while player.is_alive() and enemy.is_alive():
        print("-" * 40)
        print(f"Your HP: {player.current_hp}/{player.max_hp} | Potions: {player.potions}")
        print(f"{enemy.name}'s HP: {enemy.current_hp}/{enemy.max_hp}")
        print("\nChoose your action:")
        print("1. Attack")
        print("2. Use Potion")
        print("3. Attempt to Flee")

        choice = input("Enter 1, 2 or 3: ").strip()

        if choice == "1":
            damage = enemy.take_damage(player.attack)
            print(f"\nYou strike the {enemy.name} for {damage} damage!")
        elif choice == "2":
            healed = player.heal()
            if healed > 0:
                print(f"\nYou used a potion and healed for {healed} HP!")
            else:
                print("\nYou have no potions left!")
        elif choice == "3":
            if random.random() < 0.5:
                print("\nYou successfully fled from battle!")
                return "fled"
            else:
                print("\nYou failed to flee!")
        else:
            print("\nInvalid choice. You hesitate...")
            continue

        # Enemy turn if it's still alive
        if enemy.is_alive():
            enemy_attack = enemy.attack_value()
            damage_taken = player.take_damage(enemy_attack)
            print(f"The {enemy.name} attacks and deals {damage_taken} damage!")
            time.sleep(1)
