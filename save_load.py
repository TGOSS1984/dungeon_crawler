import json
import os
from player import Player

SAVE_FILE = "data/save.json"

# Modify save date to include room progress

def save_game(player, room_count=0, path=SAVE_FILE):
    data = {
        "player": player.to_dict(),
        "room_count": room_count
    }
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        print("\n💾 Game saved successfully.")
    except Exception as e:
        print(f"\n⚠️ Error saving game: {e}")

# Modify load date to include room progress

def load_game(path=SAVE_FILE):
    if not os.path.exists(path):
        print("\n⚠️ No save file found.")
        return None, 0

    try:
        with open(path, "r") as f:
            data = json.load(f)
        player = Player.from_dict(data["player"])
        room_count = data.get("room_count", 0)
        print(f"\n🔄 Game loaded. Welcome back, {player.name}!")
        return player, room_count
    except Exception as e:
        print(f"\n⚠️ Failed to load game: {e}")
        return None, 0
