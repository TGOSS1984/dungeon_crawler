import random

# Enemy class/stats

BOSS_NAME = "Undead King"  # define boss so cannot be fought randomly in rooms


class Enemy:
    ENEMY_TYPES = {
        "Skeleton": {"hp": 30, "attack": 8, "defence": 2},
        "Goblin": {"hp": 40, "attack": 10, "defence": 3},
        "Dark Mage": {"hp": 50, "attack": 12, "defence": 4},
        "Orc": {"hp": 60, "attack": 14, "defence": 6},
        "Wraith": {"hp": 45, "attack": 16, "defence": 2},
        BOSS_NAME: {"hp": 100, "attack": 20, "defence": 8},  # end boss stats
    }

    def __init__(self, name):
        if name not in Enemy.ENEMY_TYPES:
            raise ValueError(f"Unknown enemy type: {name}")

        stats = Enemy.ENEMY_TYPES[name]
        self.name = name
        self.max_hp = stats["hp"]
        self.current_hp = stats["hp"]
        self.attack = stats["attack"]
        self.defence = stats["defence"]

    # Enemy damage calculation and show stats

    def is_alive(self):
        return self.current_hp > 0

    def take_damage(self, amount):
        damage = max(amount - self.defence, 1)
        self.current_hp = max(self.current_hp - damage, 0)
        return damage

    def attack_value(self):
        return random.randint(self.attack - 2, self.attack + 2)

    def show_stats(self):
        print(f"\n=== Enemy: {self.name} ===")
        print(f"HP: {self.current_hp}/{self.max_hp}")
        print(f"Attack: {self.attack} | Defence: {self.defence}\n")


# random enemy generator


def generate_random_enemy():
    # Exclude the final boss from normal encounters
    enemy_names = [name for name in Enemy.ENEMY_TYPES if name != "Undead King"]
    enemy_name = random.choice(enemy_names)
    return Enemy(enemy_name)
