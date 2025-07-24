import random

# Enemy class/stats

class Enemy:
    ENEMY_TYPES = {
        "Skeleton": {"hp": 30, "attack": 8, "defence": 2},
        "Goblin": {"hp": 40, "attack": 10, "defence": 3},
        "Dark Mage": {"hp": 50, "attack": 12, "defence": 4},
        "Orc": {"hp": 60, "attack": 14, "defence": 6},
        "Wraith": {"hp": 45, "attack": 16, "defence": 2}
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
