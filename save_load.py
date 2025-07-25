import json
import os
from player import Player

SAVE_FILE = "data/save.json"

# Save game data to JSON, including room progress


def save_game(player, room_count=0, path=SAVE_FILE):
    data = {"player": player.to_dict(), "room_count": room_count}
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        print("\n💾 A whisper in the dark... your tale has been inscribed.")
    except Exception as e:
        print(f"\n⚠️ The arcane seal failed. Save error: {e}")


# Load game data from save file (JSON), restoring player and room


def load_game(path=SAVE_FILE):
    if not os.path.exists(path):
        print("\n📜 No echoes of your past were found.")
        return None, 0

    try:
        with open(path, "r") as f:
            data = json.load(f)
        player = Player.from_dict(data["player"])
        room_count = data.get("room_count", 0)
        print(f"\n🔄 Your memory stirs... Welcome back, {player.name}.")
        return player, room_count
    except Exception as e:
        print(f"\n⚠️ The memory could not be restored: {e}")
        return None, 0
