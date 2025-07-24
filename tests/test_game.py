import unittest
from player import Player
from enemies import generate_random_enemy, Enemy

# Tests for player & enemy functionality
class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("TestHero", "Warrior")

    def test_player_creation(self):
        self.assertEqual(self.player.name, "TestHero")
        self.assertEqual(self.player.player_class, "Warrior")
        self.assertEqual(self.player.current_hp, self.player.max_hp)

    def test_take_damage(self):
        original_hp = self.player.current_hp
        damage = self.player.take_damage(20)
        self.assertTrue(damage >= 1)
        self.assertEqual(self.player.current_hp, original_hp - damage)

    def test_heal(self):
        self.player.current_hp -= 20
        potions_before = self.player.potions
        healed = self.player.heal()
        self.assertTrue(healed > 0)
        self.assertEqual(self.player.potions, potions_before - 1)

    def test_add_to_inventory(self):
        self.player.add_to_inventory("Gemstone")
        self.assertIn("Gemstone", self.player.inventory)

class TestEnemy(unittest.TestCase):

    def test_generate_random_enemy(self):
        enemy = generate_random_enemy()
        self.assertIsInstance(enemy, Enemy)
        self.assertNotEqual(enemy.name, "Undead King")  # Boss should be excluded

    def test_enemy_damage(self):
        enemy = Enemy("Goblin")
        hp_before = enemy.current_hp
        damage = enemy.take_damage(10)
        self.assertTrue(damage >= 1)
        self.assertEqual(enemy.current_hp, hp_before - damage)

if __name__ == '__main__':
    unittest.main()
