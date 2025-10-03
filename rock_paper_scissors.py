"""
Rock Paper Scissors Game with All-Time Statistics

A feature-rich rock-paper-scissors game that includes:
- Best 2 out of 3 match format
- Shortcut inputs (r/p/s or full words)
- Visual game history with emojis
- Computer personality with dynamic taunts
- Persistent all-time statistics tracking
- Automatic save/load functionality

Author: Fatripod
Version: 2.1
"""

import random
import json
import os
from typing import Dict, List, Tuple, Optional, Union


class RockPaperScissorsGame:
    """Main game class that handles all rock-paper-scissors functionality."""
    
    def __init__(self, stats_filename: str = "rps_stats.json") -> None:
        """
        Initialize the game with statistics tracking.
        
        Args:
            stats_filename: Name of the file to store statistics
        """
        self.stats_filename = stats_filename
        self.shortcuts = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
        self.choices = ['rock', 'paper', 'scissors']
        self.emojis = {'rock': '🪨', 'paper': '📄', 'scissors': '✂️'}
        self.stats = self._load_all_time_stats()
        
        # Computer taunt messages
        self.computer_win_taunts = [
            "🤖 Got to try harder than that!",
            "🤖 Too easy! I saw that coming!",
            "🤖 My circuits are superior!",
            "🤖 Better luck next time, human!",
            "🤖 That's how it's done!",
            "🤖 I'm programmed to win!",
            "🤖 Nice try, but I'm faster!"
        ]
        
        self.user_win_taunts = [
            "🤖 You got me this round!",
            "🤖 Not bad... for a human.",
            "🤖 Lucky shot!",
            "🤖 I'll get you next time!",
            "🤖 My algorithms need updating...",
            "🤖 Impressive! But I'm learning!",
            "🤖 You're getting better at this!"
        ]
        
        self.tie_taunts = [
            "🤖 Great minds think alike!",
            "🤖 We're perfectly matched!",
            "🤖 Looks like we're both smart!",
            "🤖 A draw? Impossible!",
            "🤖 We think the same way!",
            "🤖 Tied again? What are the odds?",
            "🤖 Copy cat! Stop reading my mind!"
        ]

    def _get_default_stats(self) -> Dict[str, int]:
        """Get default statistics structure."""
        return {
            "matches_won": 0,
            "matches_lost": 0,
            "total_matches": 0,
            "rounds_won": 0,
            "rounds_lost": 0,
            "rounds_tied": 0,
            "total_rounds": 0
        }

    def _load_all_time_stats(self) -> Dict[str, int]:
        """Load statistics from save file or create default stats."""
        try:
            if os.path.exists(self.stats_filename):
                with open(self.stats_filename, 'r') as f:
                    return json.load(f)
            else:
                return self._get_default_stats()
        except (json.JSONDecodeError, IOError):
            print("⚠️ Could not load stats file. Starting fresh!")
            return self._get_default_stats()

    def _save_all_time_stats(self) -> None:
        """Save statistics to file."""
        try:
            with open(self.stats_filename, 'w') as f:
                json.dump(self.stats, f, indent=2)
        except IOError:
            print("⚠️ Could not save stats file.")

    def reset_statistics(self) -> bool:
        """
        Reset all statistics to zero with confirmation.
        
        Returns:
            bool: True if stats were reset, False if cancelled
        """
        print("\n" + "="*50)
        print("⚠️  RESET ALL-TIME STATISTICS")
        print("="*50)
        print("This will permanently delete all your game statistics:")
        print(f"• {self.stats['total_matches']} total matches played")
        print(f"• {self.stats['matches_won']} matches won")
        print(f"• {self.stats['total_rounds']} total rounds played")
        print(f"• All win rates and progress")
        print("\n🚨 This action CANNOT be undone!")
        
        # Double confirmation
        confirm1 = input("\nAre you sure you want to reset? (yes/no): ").lower().strip()
        if confirm1 not in ['yes', 'y']:
            print("❌ Reset cancelled.")
            return False
        
        confirm2 = input("Type 'RESET' to confirm (case-sensitive): ").strip()
        if confirm2 != 'RESET':
            print("❌ Reset cancelled - confirmation text didn't match.")
            return False
        
        # Perform the reset
        self.stats = self._get_default_stats()
        self._save_all_time_stats()
        
        print("\n✅ Statistics have been reset!")
        print("🤖 Fresh start, human! Let's see if you can do better this time!")
        print("="*50)
        return True

    def show_main_menu(self) -> str:
        """
        Display main menu and get user choice.
        
        Returns:
            str: User's menu choice
        """
        print("\n" + "="*40)
        print("🎮 MAIN MENU")
        print("="*40)
        print("1. 🎯 Play Game")
        print("2. 📊 View Statistics") 
        print("3. 🔄 Reset Statistics")
        print("4. 🚪 Quit")
        print("="*40)
        
        while True:
            choice = input("Enter your choice (1-4): ").strip()
            if choice in ['1', '2', '3', '4']:
                return choice
            print("Invalid choice! Please enter 1, 2, 3, or 4.")

    def get_user_choice(self) -> str:
        """Get the user's choice with shortcut support (r/p/s or full words)."""
        while True:
            choice = input("Enter your choice (r/rock, p/paper, s/scissors): ").lower().strip()
            
            if choice in self.shortcuts:
                return self.shortcuts[choice]
            elif choice in self.choices:
                return choice
            else:
                print("Invalid choice! Please try again.")

    def get_computer_choice(self) -> str:
        """Generate random computer choice."""
        return random.choice(self.choices)

    def determine_winner(self, user: str, computer: str) -> str:
        """Determine winner based on rock-paper-scissors rules."""
        if user == computer:
            return "tie"
        elif (user == 'rock' and computer == 'scissors') or \
             (user == 'paper' and computer == 'rock') or \
             (user == 'scissors' and computer == 'paper'):
            return "user"
        else:
            return "computer"

    def get_computer_taunt(self, result: str) -> str:
        """Get random computer taunt based on round result."""
        if result == "computer":
            return random.choice(self.computer_win_taunts)
        elif result == "user":
            return random.choice(self.user_win_taunts)
        else:  # tie
            return random.choice(self.tie_taunts)

    def get_choice_emoji(self, choice: str) -> str:
        """Get emoji for game choice."""
        return self.emojis[choice]

    def display_game_history(self, rounds_history: List[Tuple[str, str, str]]) -> None:
        """Display table of all rounds in current match."""
        if not rounds_history:
            return
        
        print("\n" + "="*35)
        print("📊 CURRENT MATCH HISTORY:")
        print("="*35)
        print(f"{'You':<12} | {'Computer':<12} | Result")
        print("-" * 35)
        
        for user_choice, computer_choice, result in rounds_history:
            user_display = f"{self.get_choice_emoji(user_choice)} {user_choice}"
            computer_display = f"{self.get_choice_emoji(computer_choice)} {computer_choice}"
            
            if result == "user":
                result_display = "🎉 You"
            elif result == "computer":
                result_display = "🤖 CPU"
            else:
                result_display = "🤝 Tie"
            
            print(f"{user_display:<12} | {computer_display:<12} | {result_display}")
        
        print("="*35)

    def get_final_taunt(self, user_wins: int, computer_wins: int) -> str:
        """Get final taunt for end of match."""
        if user_wins == 2:
            final_taunts = [
                "🤖 Well played, human! You've earned this victory!",
                "🤖 I admit defeat... this time!",
                "🤖 You're better than I calculated!",
                "🤖 Congratulations! But I demand a rematch!",
                "🤖 My programming didn't account for your skill!"
            ]
        else:
            final_taunts = [
                "🤖 Victory is mine! As calculated!",
                "🤖 Better luck next time, human!",
                "🤖 My superior logic wins again!",
                "🤖 Maybe you should upgrade your brain!",
                "🤖 I am the ultimate rock-paper-scissors machine!"
            ]
        
        return random.choice(final_taunts)

    def display_all_time_stats(self) -> None:
        """Display formatted all-time statistics."""
        print("\n" + "="*45)
        print("🏆 ALL-TIME STATISTICS")
        print("="*45)
        print(f"Matches Won:     {self.stats['matches_won']}")
        print(f"Matches Lost:    {self.stats['matches_lost']}")
        print(f"Total Matches:   {self.stats['total_matches']}")
        
        if self.stats['total_matches'] > 0:
            win_rate = (self.stats['matches_won'] / self.stats['total_matches']) * 100
            print(f"Win Rate:        {win_rate:.1f}%")
        else:
            print("Win Rate:        N/A (no matches played)")
        
        print(f"\nRounds Won:      {self.stats['rounds_won']}")
        print(f"Rounds Lost:     {self.stats['rounds_lost']}")
        print(f"Rounds Tied:     {self.stats['rounds_tied']}")
        print(f"Total Rounds:    {self.stats['total_rounds']}")
        
        if self.stats['total_rounds'] > 0:
            round_win_rate = (self.stats['rounds_won'] / self.stats['total_rounds']) * 100
            print(f"Round Win Rate:  {round_win_rate:.1f}%")
        else:
            print("Round Win Rate:  N/A (no rounds played)")
        
        print("="*45)

    def display_victory_trophy(self) -> None:
        """Display ASCII art trophy when user wins a match."""
        trophy_art = r"""
        
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
        """
        
        # Clear effect with spacing
        print("\n" * 3)
        print(trophy_art)
        print("\n" * 2)
        
        # Victory sound effect (text-based)
        print("🎺 *TRUMPET FANFARE* 🎺")
        print("🎊 *CONFETTI FALLING* 🎊")
        print("👏 *CROWD CHEERING* 👏")
        print("\n")

    def play_best_of_three(self) -> None:
        """Play a complete best-of-3 match and update statistics."""
        user_wins = 0
        computer_wins = 0
        round_num = 1
        rounds_history: List[Tuple[str, str, str]] = []
        
        print("=== Best 2 out of 3 Rock Paper Scissors ===")
        print("🤖 Prepare to face my superior algorithms!")
        
        while user_wins < 2 and computer_wins < 2:
            print(f"\n--- Round {round_num} ---")
            print(f"Score: You {user_wins} - {computer_wins} Computer")
            
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            
            result = self.determine_winner(user_choice, computer_choice)
            rounds_history.append((user_choice, computer_choice, result))
            
            # Update round stats
            self.stats['total_rounds'] += 1
            if result == "user":
                self.stats['rounds_won'] += 1
            elif result == "computer":
                self.stats['rounds_lost'] += 1
            else:
                self.stats['rounds_tied'] += 1
            
            self.display_game_history(rounds_history)
            
            if result == "tie":
                print("🤝 It's a tie!")
            elif result == "user":
                print("🎉 You win this round!")
                user_wins += 1
            else:
                print("🤖 Computer wins this round!")
                computer_wins += 1
            
            print(self.get_computer_taunt(result))
            round_num += 1
        
        # Update match stats
        self.stats['total_matches'] += 1
        if user_wins == 2:
            self.stats['matches_won'] += 1
        else:
            self.stats['matches_lost'] += 1
        
        print("\n" + "="*40)
        if user_wins == 2:
            # Display the trophy screen for user victory!
            self.display_victory_trophy()
            print("🏆 VICTORY! You won the best 2 out of 3!")
        else:
            print("🤖 Computer won the best 2 out of 3!")
        print(f"Final Score: You {user_wins} - {computer_wins} Computer")
        
        print(self.get_final_taunt(user_wins, computer_wins))
        print("="*40)
        
        self._save_all_time_stats()

    def run(self) -> None:
        """Main game loop with menu system."""
        print("🎮 Welcome to Rock Paper Scissors!")
        
        while True:
            choice = self.show_main_menu()
            
            if choice == '1':  # Play Game
                self.play_best_of_three()
                
            elif choice == '2':  # View Statistics
                if self.stats['total_matches'] > 0:
                    self.display_all_time_stats()
                else:
                    print("\n📊 No statistics yet - play your first game!")
                    
            elif choice == '3':  # Reset Statistics
                self.reset_statistics()
                
            elif choice == '4':  # Quit
                print("\nThanks for playing! Goodbye! 👋")
                if self.stats['total_matches'] > 0:
                    print("Your stats have been saved!")
                break


def main() -> None:
    """Entry point for the game."""
    game = RockPaperScissorsGame()
    game.run()


if __name__ == "__main__":
    main()
