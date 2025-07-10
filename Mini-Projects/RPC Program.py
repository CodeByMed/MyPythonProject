import random

class RockPaperScissorsGame:
    """
    A console-based Rock, Paper, Scissors game against a computer AI.
    The AI randomly selects one of the three options each round.
    The player competes to win rounds and can replay as desired.
    """

    def __init__(self):
        """Initializes game options, score tracking, and placeholders for player/computer choices."""
        self.options = ["Rock", "Paper", "Scissors"]
        self.player_choice = None
        self.computer_choice = None
        self.player_score = 0
        self.computer_score = 0

    def get_player_input(self):
        """Prompts the player for input until a valid option is entered."""
        while True:
            choice = input("Choose (Rock, Paper, Scissors): ").capitalize().strip()
            if choice in self.options:
                self.player_choice = choice
                break
            print("Invalid choice. Please enter Rock, Paper, or Scissors.")

    def get_computer_choice(self):
        """Randomly selects a choice for the computer."""
        self.computer_choice = random.choice(self.options)

    def decide_winner(self):
        """
        Compares player and computer choices to determine the winner of the round.
        Updates scores accordingly and prints the result.
        """
        print(f"\nYou chose: {self.player_choice}")
        print(f"Computer chose: {self.computer_choice}")

        if self.player_choice == self.computer_choice:
            print("It's a tie!")
        elif (
            (self.player_choice == "Rock" and self.computer_choice == "Scissors") or
            (self.player_choice == "Paper" and self.computer_choice == "Rock") or
            (self.player_choice == "Scissors" and self.computer_choice == "Paper")
        ):
            print("You win this round!")
            self.player_score += 1
        else:
            print("Computer wins this round!")
            self.computer_score += 1

    def show_score(self):
        """Displays the current score."""
        print(f"\nScore => You: {self.player_score} | Computer: {self.computer_score}\n")

    def play_round(self):
        """Plays a single round of the game."""
        self.get_player_input()
        self.get_computer_choice()
        self.decide_winner()
        self.show_score()

    def ask_replay(self):
        """Asks the player if they want to play again."""
        while True:
            answer = input("Play again? (y/n): ").lower().strip()
            if answer in ("y", "n"):
                return answer == "y"
            print("Please enter 'y' or 'n'.")

    def run(self):
        """Starts the game loop."""
        print("=== Rock, Paper, Scissors ===")
        while True:
            self.play_round()
            if not self.ask_replay():
                print("Thanks for playing! Final Score => You: {} | Computer: {}\nGoodbye!".format(
                    self.player_score, self.computer_score
                ))
                break

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.run()
