import random

# Player / class stats with a dark fantasy twist


class Player:
    CLASS_STATS = {
        "Oathbound Knight": {"max_hp": 130, "attack": 15, "defence": 10, "potions": 2},
        "Shadow Pilgrim": {"max_hp": 100, "attack": 18, "defence": 7, "potions": 3},
        "Ashen Scholar": {"max_hp": 80, "attack": 22, "defence": 5, "potions": 4},
        "Hollow Marksman": {"max_hp": 110, "attack": 17, "defence": 6, "potions": 3},
    }

    def __init__(self, name, player_class):
        if player_class not in Player.CLASS_STATS:
            raise ValueError(f"Invalid class: {player_class}")

        self.name = name
        self.player_class = player_class
        stats = Player.CLASS_STATS[player_class]

        self.max_hp = stats["max_hp"]
        self.current_hp = self.max_hp
        self.attack = stats["attack"]
        self.defence = stats["defence"]
        self.potions = stats["potions"]
        self.gold = 0
        self.inventory = []

    # Damage calculation - takes defence stat into account

    def is_alive(self):
        return self.current_hp > 0

    def take_damage(self, amount):
        damage = max(amount - self.defence, 1)
        self.current_hp = max(self.current_hp - damage, 0)
        return damage

    # Healing logic - heals for random amount between 15 & 30 hp & decrements
    # potions if greater than 0 by 1 once used

    def heal(self):
        if self.potions > 0:
            heal_amount = random.randint(15, 30)
            self.current_hp = min(self.current_hp + heal_amount, self.max_hp)
            self.potions -= 1
            return heal_amount
        else:
            return 0

    # Function for adding items to inventory

    def add_to_inventory(self, item):
        self.inventory.append(item)

    # Show stats function with themed formatting

    def show_stats(self):
        print(f"\n=== {self.name}, the {self.player_class} ===")
        print(f"Vitality: {self.current_hp}/{self.max_hp}")
        print(f"Strength: {self.attack} | Resilience: {self.defence}")
        print(f"Estus: {self.potions} | Souls: {self.gold}")
        print(
            f"Inventory: {
                ', '.join(
                    self.inventory) if self.inventory else 'Empty'}\n")

    def to_dict(self):
        return {
            "name": self.name,
            "player_class": self.player_class,
            "max_hp": self.max_hp,
            "current_hp": self.current_hp,
            "attack": self.attack,
            "defence": self.defence,
            "potions": self.potions,
            "gold": self.gold,
            "inventory": self.inventory,
        }

    # Data to support save/load via JSON

    @classmethod
    def from_dict(cls, data):
        player = cls(data["name"], data["player_class"])
        player.max_hp = data["max_hp"]
        player.current_hp = data["current_hp"]
        player.attack = data["attack"]
        player.defence = data["defence"]
        player.potions = data["potions"]
        player.gold = data["gold"]
        player.inventory = data["inventory"]
        return player
