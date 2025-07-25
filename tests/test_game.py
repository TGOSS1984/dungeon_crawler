import unittest
from player import Player
from enemies import generate_random_enemy, Enemy
from unittest.mock import patch
from battle import battle
import tempfile
import shutil
import os
from save_load import save_game, load_game, SAVE_FILE
from itertools import cycle


# Tests for player & enemy functionality
class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("TestKnight", "Oathbound Knight")

    def test_player_creation(self):
        self.assertEqual(self.player.name, "TestKnight")
        self.assertEqual(self.player.player_class, "Oathbound Knight")
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
        self.player.add_to_inventory("Cursed Ember")
        self.assertIn("Cursed Ember", self.player.inventory)


class TestEnemy(unittest.TestCase):

    def test_generate_random_enemy(self):
        enemy = generate_random_enemy()
        self.assertIsInstance(enemy, Enemy)
        self.assertNotEqual(enemy.name, "Undead King")  # Boss should be excluded

    def test_enemy_damage(self):
        enemy = Enemy("Ashen Wretch")
        hp_before = enemy.current_hp
        damage = enemy.take_damage(10)
        self.assertTrue(damage >= 1)
        self.assertEqual(enemy.current_hp, hp_before - damage)


if __name__ == "__main__":
    unittest.main()


# Battle loop tests


class TestBattle(unittest.TestCase):

    @patch(
        "builtins.input", side_effect=cycle(["1"])
    )  # Updated this to cycle through inputs so battle can finished aftre increased enemy hp
    def test_battle_victory(self, mock_input):
        player = Player("Duskblade", "Shadow Pilgrim")
        enemy = Enemy("Carrion Spawn")
        result = battle(player, enemy)
        self.assertIn(result, ["won", "lost", "fled"])


# Save/Load test
class TestSaveLoad(unittest.TestCase):

    def setUp(self):
        self.player = Player("SaveTester", "Ashen Scholar")
        self.temp_dir = tempfile.mkdtemp()
        self.test_path = os.path.join(self.temp_dir, "save.json")

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_save_and_load_game(self):
        save_game(self.player, room_count=4, path=self.test_path)
        loaded_player, loaded_room = load_game(path=self.test_path)
        self.assertEqual(loaded_player.name, self.player.name)
        self.assertEqual(loaded_player.player_class, self.player.player_class)
        self.assertEqual(loaded_room, 4)


# Test invalid inputs
class TestErrorHandling(unittest.TestCase):

    def test_invalid_class_raises(self):
        with self.assertRaises(ValueError):
            Player("Hero", "InvalidClass")


@patch("builtins.input", side_effect=["", "  ", "Hero"])
def test_name_retry_on_empty_input(self, mock_input):
    from main import get_player_name

    name = get_player_name()
    self.assertEqual(name, "Hero")
