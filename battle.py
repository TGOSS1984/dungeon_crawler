from utils import red, green, yellow, bold  # for text cols
from enemies import Enemy
from player import Player
import random
import time

# Enemy appears note with logic for turn based battle, pick from 3 options


def battle(player, enemy):
    print(bold(f"\n⚔️ A wretched {enemy.name} emerges from the shadows..."))
    enemy.show_stats()

    while player.is_alive() and enemy.is_alive():
        print("-" * 40)
        print(
            f"Your Vitality: {player.current_hp}/{player.max_hp} | Estus Flasks: {player.potions}"
        )
        print(f"{enemy.name}'s Essence: {enemy.current_hp}/{enemy.max_hp}")
        print("\nChoose your action:")
        print("1. Deliver a Strike")
        print("2. Use Estus Flask")
        print("3. Attempt to Flee")

        choice = input("Enter 1, 2 or 3: ").strip()

        if choice == "1":
            damage = enemy.take_damage(player.attack)
            if damage > 15:
                print(
                    bold(
                        f"\n⚡ You land a staggering blow! {enemy.name} reels from {damage} damage!"
                    )
                )
            else:
                print(f"\nYou slash into the {enemy.name}, dealing {damage} damage.")
        elif choice == "2":
            healed = player.heal()
            if healed > 0:
                print(
                    green(
                        f"\n✨ You sip from a cracked Estus Flask, restoring {healed} Vitality..."
                    )
                )
            else:
                print(red("\nYour flasks are dry. No healing remains."))
        elif choice == "3":
            if random.random() < 0.5:
                print(
                    yellow(
                        "\nYou retreat into the mist. The enemy fades into the dark..."
                    )
                )
                return "fled"
            else:
                print(red("\nYour escape fails. The way is blocked!"))
        else:
            print("\nYou hesitate... and the enemy advances.")
            continue

        # Enemy's turn if still alive
        if enemy.is_alive():
            enemy_attack = enemy.attack_value()
            damage_taken = player.take_damage(enemy_attack)
            print(
                red(
                    f"The {enemy.name} strikes with fury, dealing {damage_taken} damage!"
                )
            )
            time.sleep(1)

    # Battle outcome
    print("\n" + "=" * 40)
    if player.is_alive():
        print(green(f"\n✅ The {enemy.name} crumbles to ash."))
        gold_reward = random.randint(5, 15)
        player.gold += gold_reward
        print(yellow(f"You absorb {gold_reward} lost souls."))
        return "won"
    else:
        print(red("💀 You fall to your knees... and the light fades."))
        return "lost"
