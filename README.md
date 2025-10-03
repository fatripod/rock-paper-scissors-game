``` markdown
# 🏆 Rock Paper Scissors Championship Game

A feature-rich, terminal-based Rock Paper Scissors game with ASCII art celebrations, persistent statistics, and a sassy computer opponent!

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Game](https://img.shields.io/badge/game-rock%20paper%20scissors-red.svg)

## 🎮 Features

### Core Game
- **Best 2 out of 3 matches** - Classic tournament format
- **Smart input system** - Use shortcuts (`r`/`p`/`s`) or full words
- **Visual game history** - See all your moves with emojis 🪨📄✂️
- **Epic ASCII trophy** - Celebrate victories in style!

### Computer Opponent
- **Dynamic personality** - Trash talks and celebrates
- **Contextual taunts** - Different messages for wins, losses, and ties
- **Victory celebrations** - Computer gloats when it wins

### Statistics & Progress
- **Persistent stats tracking** - All your games are remembered
- **Match & round statistics** - Detailed win/loss records
- **Win rate calculations** - Track your improvement
- **Safe reset option** - Double-confirmation to reset stats

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Terminal/Command Prompt

### Installation & Run
1. **Download the game:**
   ```bash
   git clone https://github.com/fatripod/rock-paper-scissors-game.git
   cd rock-paper-scissors-game
   ```

2. **Run the game:**
   ```bash
   python rock_paper_scissors.py
   ```

3. **Start playing!** 🎯

## 🎲 How to Play

### Basic Controls
- **Choose your weapon:** Type `r`, `p`, `s` OR `rock`, `paper`, `scissors`
- **Menu navigation:** Use numbers 1-4 in the main menu
- **Win condition:** First to win 2 rounds wins the match!

### Game Rules
- 🪨 **Rock** crushes ✂️ **Scissors**
- 📄 **Paper** covers 🪨 **Rock**  
- ✂️ **Scissors** cuts 📄 **Paper**

## 🎨 Game Screenshots & Interface

### Main Menu
```

🎮 Welcome to Rock Paper Scissors!
======================================== 🎮 MAIN MENU ========================================
🎯 Play Game
📊 View Statistics
🔄 Reset Statistics
🚪 Quit ======================================== Enter your choice (1-4):``` 

### Game Match Start
```

=== Best 2 out of 3 Rock Paper Scissors === 🤖 Prepare to face my superior algorithms!
--- Round 1 --- Score: You 0 - 0 Computer Enter your choice (r/rock, p/paper, s/scissors): r``` 

### Current Match History Display
```

=================================== 📊 CURRENT MATCH HISTORY: =================================== You | Computer | Result
 
🪨 rock | ✂️ scissors | 🎉 You 📄 paper | 🪨 rock | 🎉 You ===================================
🎉 You win this round! 🤖 You got me this round!``` 

### Statistics Screen
```

============================================= 🏆 ALL-TIME STATISTICS ============================================= Matches Won: 5 Matches Lost: 3 Total Matches: 8 Win Rate: 62.5%
Rounds Won: 12 Rounds Lost: 9 Rounds Tied: 2 Total Rounds: 23 Round Win Rate: 52.2% =============================================``` 

### Reset Statistics Warning
```

================================================== ⚠️ RESET ALL-TIME STATISTICS ================================================== This will permanently delete all your game statistics: • 8 total matches played • 5 matches won • 23 total rounds played • All win rates and progress
🚨 This action CANNOT be undone!
Are you sure you want to reset? (yes/no): yes Type 'RESET' to confirm (case-sensitive): RESET
✅ Statistics have been reset! 🤖 Fresh start, human! Let's see if you can do better this time! ==================================================``` 

## 🏆 Victory Celebration Screen

When you defeat the computer, you'll be treated to this epic ASCII art trophy display:
```

🏆 CONGRATULATIONS! YOU ARE THE CHAMPION! 🏆
               ___________
              '._==_==_=_.'
              .-\:      /-.
             | (|:.     |) |
              '-|:.     |-'
                \::.    /
                 '::. .'
                   ) (
                 _.' '._
                `"""""""`

  ╔══════════════════════════════════════╗
  ║        🎉 VICTORY ACHIEVED! 🎉       ║
  ║                                      ║
  ║    You have defeated the computer    ║
  ║       in this epic battle of         ║
  ║       Rock, Paper, Scissors!         ║
  ║                                      ║
  ║      🤖 → 😵 Computer Status         ║
  ║      🧠 → 💪 Your Brain Power        ║
  ║      🎯 → ✨ Victory Unlocked        ║
  ╚══════════════════════════════════════╝

🌟 You have proven your superiority! 🌟
🎺 TRUMPET FANFARE 🎺 🎊 CONFETTI FALLING 🎊 👏 CROWD CHEERING 👏
======================================== 🏆 VICTORY! You won the best 2 out of 3! Final Score: You 2 - 1 Computer 🤖 Well played, human! You've earned this victory! ========================================``` 

### Computer Victory (When You Lose)
```

======================================== 🤖 Computer won the best 2 out of 3! Final Score: You 1 - 2 Computer 🤖 Victory is mine! As calculated! ========================================``` 

### Complete Game Session Example
```

🎮 Welcome to Rock Paper Scissors!
======================================== 🎮 MAIN MENU ========================================
🎯 Play Game
📊 View Statistics
🔄 Reset Statistics
🚪 Quit ======================================== Enter your choice (1-4): 1
=== Best 2 out of 3 Rock Paper Scissors === 🤖 Prepare to face my superior algorithms!
--- Round 1 --- Score: You 0 - 0 Computer Enter your choice (r/rock, p/paper, s/scissors): r
=================================== 📊 CURRENT MATCH HISTORY: =================================== You | Computer | Result
 
🪨 rock | ✂️ scissors | 🎉 You
🎉 You win this round! 🤖 You got me this round!
--- Round 2 --- Score: You 1 - 0 Computer Enter your choice (r/rock, p/paper, s/scissors): p
=================================== 📊 CURRENT MATCH HISTORY: =================================== You | Computer | Result
 
🪨 rock | ✂️ scissors | 🎉 You 📄 paper | 🪨 rock | 🎉 You ===================================
🎉 You win this round! 🤖 Not bad... for a human.
[VICTORY TROPHY SCREEN DISPLAYS HERE]
======================================== 🏆 VICTORY! You won the best 2 out of 3! Final Score: You 2 - 0 Computer 🤖 I admit defeat... this time! ========================================``` 

## 📊 Statistics Tracking

The game automatically tracks your performance:
- **Match statistics** - Total wins/losses and win rate
- **Round statistics** - Individual round performance  
- **Persistent storage** - Stats saved between sessions in `rps_stats.json`
- **Safe reset** - Reset stats with double confirmation

## 🤖 Meet Your Opponent

The computer isn't just random - it has personality! Expect different responses:

### Computer Win Taunts
- *"🤖 Got to try harder than that!"*
- *"🤖 Too easy! I saw that coming!"*
- *"🤖 My circuits are superior!"*
- *"🤖 Better luck next time, human!"*

### Computer Loss Reactions
- *"🤖 You got me this round!"*
- *"🤖 Not bad... for a human."*
- *"🤖 Lucky shot!"*
- *"🤖 My algorithms need updating..."*

### Tie Comments
- *"🤖 Great minds think alike!"*
- *"🤖 We're perfectly matched!"*
- *"🤖 Copy cat! Stop reading my mind!"*

### Final Match Taunts
**When Computer Wins:**
- *"🤖 Victory is mine! As calculated!"*
- *"🤖 My superior logic wins again!"*

**When You Win:**
- *"🤖 Well played, human! You've earned this victory!"*
- *"🤖 You're better than I calculated!"*

## 🛠️ Technical Details

### File Structure
```

rock-paper-scissors-game/ ├── rock_paper_scissors.py # Main game file ├── rps_stats.json # Stats storage (auto-created) ├── README.md # This file └── .gitignore # Git ignore rules``` 

### Dependencies
- **Built-in Python modules only:**
  - `random` - Computer choice generation
  - `json` - Statistics persistence
  - `os` - File system operations
  - `typing` - Type hints for better code

### Key Classes & Methods
- `RockPaperScissorsGame` - Main game controller
- `display_victory_trophy()` - ASCII art celebration
- `play_best_of_three()` - Match gameplay loop
- `display_game_history()` - Visual round history
- Statistics tracking with auto-save/load

## 🤝 Contributing

Found a bug or want to add a feature? Contributions are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE] file for details.

## 🙏 Acknowledgments

- Inspired by the classic Rock Paper Scissors game
- ASCII art trophy designed for maximum celebration impact
- Built with Python's simplicity and power in mind

## 🎯 Future Features

- [ ] Multiplayer mode
- [ ] Tournament brackets
- [ ] More ASCII art celebrations
- [ ] Sound effects (actual audio)
- [ ] Difficulty levels with different AI strategies
- [ ] Leaderboards
- [ ] Custom game rules (Rock Paper Scissors Lizard Spock?)

---

**Ready to become the Rock Paper Scissors Champion?** 🏆

Start playing now: `python rock_paper_scissors.py`

*May the best strategist win!* 🎮

---
*Created by [@fatripod](https://github.com/fatripod)*
```
✅ Computer personality examples ✅ Menu interactions ✅ Complete game session walkthrough
Users can see exactly what your game looks like and how it works just by reading the README! No separate screenshot files needed - everything is embedded right in the documentation. 🚀
