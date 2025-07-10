import random

class NumberGuessingGame:
    """
    A simple number guessing game where the player has to guess a randomly selected number.
    The game provides feedback and counts the number of attempts.
    """

    def __init__(self, lowest=1, highest=100):
        """
        Initialize game parameters and generate a random number.
        """
        self.lowest_num = lowest
        self.highest_num = highest
        self.number = random.randint(self.lowest_num, self.highest_num)
        self.tries = 0

    def reset_game(self):
        """
        Resets the game state for a new round.
        """
        self.number = random.randint(self.lowest_num, self.highest_num)
        self.tries = 0

    def get_user_input(self):
        """
        Safely gets an integer input from the user within the allowed range.
        """
        while True:
            try:
                guess = int(input(f"Enter a number between {self.lowest_num} and {self.highest_num}: "))
                if self.lowest_num <= guess <= self.highest_num:
                    return guess
                else:
                    print(f"⚠️ Please enter a number within the range {self.lowest_num} - {self.highest_num}.")
            except ValueError:
                print("❌ Invalid input. Please enter a valid integer.")

    def play_round(self):
        """
        Plays a single round of the guessing game.
        """
        print(f"\n🎯 I'm thinking of a number between {self.lowest_num} and {self.highest_num}. Try to guess it!")

        while True:
            guess = self.get_user_input()
            self.tries += 1

            if guess < self.number:
                print("🔻 Too low! Try again.")
            elif guess > self.number:
                print("🔺 Too high! Try again.")
            else:
                print(f"\n✅ Correct! The number was {self.number}.")
                print(f"🏆 You guessed it in {self.tries} tries.")
                break

    def run(self):
        """
        Starts the game and handles replay logic.
        """
        print("=== Welcome to the Number Guessing Game ===")

        while True:
            self.play_round()
            again = input("\n🔁 Do you want to play again? (y/n): ").strip().lower()

            if again != 'y':
                print("👋 Thanks for playing. Goodbye!")
                break
            else:
                self.reset_game()


if __name__ == "__main__":
    game = NumberGuessingGame()
    game.run()
