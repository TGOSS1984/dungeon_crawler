# Crypt of Shadows – A Python Dungeon Crawler CLI Game

This is a turn-based dungeon crawler built entirely in Python for the command line.  
It runs in the mock terminal on Heroku.

The player explores a cursed crypt, fights horrors from the abyss, collects relics, and faces off against a final boss — the Undead King. The game is driven by classes, functions, loops, file I/O, and a touch of dark fantasy.
It is meant to mimic 'Rogue-like' gameplay with random room generation and item collections.

[Github (repo) link to project](https://github.com/TGOSS1984/dungeon_crawler)

[Heroku Link to project](https://crypt-of-shadows-python-game-fccd0cae9fda.herokuapp.com/)

**Image from Heroku on Terminal**

![Image of game screen](assets/screenshots/game_terminal_mockup.PNG)

---

## Table of Contents

- [Features](#features)
- [Features](#features)
- [Features](#features)
- [Features](#features)
- [Features](#features)


---

##  Features

- Choose from four themed classes:
  - **Oathbound Knight** – High vitality and defence
  - **Shadow Pilgrim** – Balanced agility and attack
  - **Ashen Scholar** - Fragile but powerful spellcaster
  - **Hollow Marksman** - Ranged damage with stamina
- Turn-based battles against Souls-like enemies
- Estus Flask system (potions), gold, and rare items
- Traps, rest rooms, and random events in each dungeon room
- Save/load functionality via JSON file
- Final boss fight after surviving 10 rooms
- Colored text UI (using `colorama`) for a more immersive experience
- Defensive input validation and error handling
- Fully tested core modules (`player.py`, `enemies.py`, `battle.py`, `save_load.py`)

### How to Play

- Follow prompts to enter your name and select a class
- Navigate room by room, choose whether to fight, use potions, or flee
- After each room, you’ll be asked if you want to save your progress
- The game ends when you die, defeat the boss, or manually exit

### Features for future development

- Make more use for picked up items
- Add a shop to spend souls could be added to a room randomly
- Add further classes - have more variety between them, starting item, special move etc
- Add a midway point boss, and make the boss generator random

---

##  File Structure

```
dungeon_crawler/
│
├── run.py
├── main.py
├── player.py
├── enemies.py
├── battle.py
├── dungeon.py
├── save_load.py
├── utils.py
├── index.js
├── package.json
├── requirements.txt
├── .gitignore
├── runtime.txt
├── Procfile
├── readme.md
├── views/
│   ├── index.html
│   └── layout.html
├── controllers/
│   └── default.js
├── data/
│   └── save.json
├── assets/
│   └── screenshots
└── tests/
    └── test_game.py
```

---

##  Technologies Used

- Python 3
- `colorama` for terminal styling
- `unittest` and `mock` for testing
- JSON for saving/loading game state

---

##  Installation & Setup for vscode

1. Clone this repo
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```
3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the game:
   ```bash
   python main.py
   ```
### Running game on Heroku


This game is terminal-based, so it's not meant to be played in a web browser.

However, with code institutes mock terminal setup it can be played here [Heroku Link to project](https://crypt-of-shadows-python-game-fccd0cae9fda.herokuapp.com/)

---

##  Testing

All core features are covered in `tests/test_game.py`:

- Player stats, healing, inventory, damage
- Enemy generation and combat behavior
- Battle function tested via mocked user input
- Save/load tested using temporary file handling
- Error cases (e.g. invalid class selection, empty name input) are also tested

Run tests (in terminal) with:

```bash
python -m unittest discover tests
```
```bash
python -m unittest tests/test_game.py
```

### Tested in Python code linter

Code throughout the project has been checked and cleaned to ensure it meets **PEP8 standards**.

- **[pep8ci.herokuapp.com](https://pep8ci.herokuapp.com/#)** was used for manual checks.

- **`black`** was installed and used to auto-format the project:  
  Run `pip install black` and `black .`

Examples of some of the issues I came across using manual python code checks:

- `E501`: **Line too long**
- `E122`: **Continuation line missing indentation**
- `E302`: **Expected 2 blank lines before top-level function/class**
- `W291`: **Trailing whitespace**
- `W293`: **Blank line contains whitespace**

###  Bugs I Encountered (and fixed) & Manual Testing

Examples below of bugs I encountered and ultimately fixed. Alongside these fixes regular print statements were used to try and troubleshoot any issues as they arose.

**Boss Appeared Randomly in Early Rooms**
Originally, the "Undead King" could spawn in regular rooms (not just the end).  
→ I fixed this by excluding the boss from the random enemy generator using a filtered list.

**Game Didn’t Resume from the Correct Room**
When I added the save feature, it saved the player stats — but restarted back at room 1.  
→ I updated the save/load functions to also store `room_count` so progress could resume properly.

**SAVE_FILE Error in Testing**
I tried to test the save function using a temp file but hit an `UnboundLocalError` with `SAVE_FILE`.  
→ Refactored `save_game()` and `load_game()` to accept a custom path — much easier to test now.

**Wrong Variable Case: `Name` not `name`**
Got a `NameError` on player creation because I accidentally capitalized `Name`.  
→ Simple typo fix in `player.py`.

**Dungeon Not Recognizing `enter_dungeon`**
Forgot to import `enter_dungeon` correctly into `main.py`, which broke the game loop.  
Added the import and that fixed it

---

##  Development Notes

- Code is modular and follows PEP8
- All inputs are validated with retry loops or graceful fallbacks
- Git used for version control from day one
- Commit history is structured around logical features and fixes

---

##  Deployment

This game is CLI-based and can run in any terminal that supports Python 3.  
**VSCode**

- Code was written using VSCode
- Folder structure all main .py files found in root. Along with requirements.txt, .gitingore, .python-version. Assests folder contains screenshots for readme, tests folder contains the .py tests file. Data folder cotnains the .json save file.

**GitHub**

- A GitHub account was created
- A new reposiory was created on GitHub by clicking the 'New' button. It was named and set as public.
- A folder was created in VSCode and initialised as a Git repository
- In VSCode the terminal was used to run commands to link the local project to the GitHub repository
- Throughout the process of builing the website, commits & pushes were staged regularly using terminal commands such as 'git add .' , 'git-commit -m' & 'git push'
- Host the project: Went to my GitHub repository, clicked settings > pages and selected the branch to publish, hit save and then GitHub generated a live link (link at top of readme)

**Deploy to Heroku**

1. **Create **`` in the root directory:

```
web: gunicorn run:app
```

2. **Add **``** to requirements.txt**:

```bash
pip install gunicorn
pip freeze > requirements.txt
```

3. **Commit and push to GitHub**

4. **On Heroku dashboard**:

   - Create a new app
   - Connect your GitHub repo under **Deploy > Deployment method**
   - Enable automatic deploys if desired
   - Click **Deploy Branch**

5. **Open App** once deployed (`https://crypt-of-shadows-python-game-fccd0cae9fda.herokuapp.com/`)


---

## Credits



