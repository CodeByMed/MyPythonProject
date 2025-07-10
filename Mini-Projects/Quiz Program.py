""" Quiz Game Program """
class QuizGame:
    def __init__(self):
        """
        Constructor: Initializes the Questions and Player Points.
        """
        self.questions = {
            "What is the capital of Bolivia?": {
                "options": ["A. Chapas", "B. La Paz", "C. Deai", "D. Bolivia City"],
                "answer": "B"
            },
            "How many continents exist?": {
                "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
                "answer": "C"
            },
            "Which chemical element has the symbol 'O'?": {
                "options": ["A. Oxygen", "B. Gold", "C. Hydrogen", "D. Carbon"],
                "answer": "A"
            }
        }
        self.score = 0

    def run(self):
        """
        Executes the Quiz.
        """
        print("Welcome to the Quiz!\n")

        for question, data in self.questions.items():
            print(f"Question: {question}")
            for option in data["options"]:
                print(option)

            user_answer = input("Your Answer (A, B, C or D): ").strip().upper()
            correct_answer = data["answer"]

            if user_answer == correct_answer:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was: {correct_answer}\n")
        self.show_result()

    def show_result(self):
        """
        Shows the final results.
        """
        print(f"\nYou answered {self.score} out of {len(self.questions)} questions correctly.")
        if self.score == len(self.questions):
            print("Well done! 🎉")
        elif self.score > 0:
            print("Good job 😊")
        else:
            print("Better luck next time... 😅")

if __name__ == "__main__":
    app = QuizGame()
    app.run()
