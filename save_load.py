import json
import os
from player import Player

SAVE_FILE = "data/save.json"

def save_game(player):
    data = player.to_dict()

    try:
        os.makedirs("data", exist_ok=True)
        with open(SAVE_FILE, "w") as f:
            json.dump(data, f, indent=4)
        print("\n💾 Game saved successfully.")
    except Exception as e:
        print(f"\n⚠️ Error saving game: {e}")

def load_game():
    if not os.path.exists(SAVE_FILE):
        print("\n⚠️ No save file found.")
        return None

    try:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
        player = Player.from_dict(data)
        print(f"\n🔄 Game loaded. Welcome back, {player.name}!")
        return player
    except Exception as e:
        print(f"\n⚠️ Failed to load game: {e}")
        return None
