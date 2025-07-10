'''Banking Application Program'''
class BankingApp:
    def __init__(self):
        """Initialize the banking app with default balance and bank reserve."""
        self.balance = 1000.0
        self.bank_reserve = 500.0

    def show_balance(self):
        """Display the current balance of the user and the bank."""
        print(f"\nYour Balance: ${self.balance:.2f}")
        print(f"Bank Reserve: ${self.bank_reserve:.2f}\n")

    def withdraw(self):
        """
        Allow the user to withdraw money from the virtual bank.
        Adjusts both user balance and bank reserve accordingly.
        """
        try:
            amount = float(input("Enter withdrawal amount: "))
            if amount <= 0:
                print("Withdrawal amount must be greater than zero.\n")
            elif amount > self.bank_reserve:
                print(f"The bank only has ${self.bank_reserve:.2f} available. Withdrawal denied.\n")
            else:
                self.bank_reserve -= amount
                self.balance += amount
                print(f"Withdrew ${amount:.2f} successfully.\n")
        except ValueError:
            print("Invalid input. Please enter a valid numeric amount.\n")

    def deposit(self):
        """
        Allow the user to deposit money into the virtual bank.
        Deducts from user balance and increases bank reserve.
        """
        try:
            amount = float(input("Enter deposit amount: "))
            if amount <= 0:
                print("Deposit amount must be greater than zero.\n")
            elif amount > self.balance:
                print("You cannot deposit more money than you currently have.\n")
            else:
                self.bank_reserve += amount
                self.balance -= amount
                print(f"Deposited ${amount:.2f} successfully.\n")
        except ValueError:
            print("Invalid input. Please enter a valid numeric amount.\n")

    def run(self):
        """
        Run the main application loop.
        Displays a menu and handles user selections.
        """
        while True:
            print("\n=== Banking Menu ===")
            print("1. Show Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Exit")

            try:
                choice = int(input("Choose an option (1-4): "))
                if choice == 1:
                    app.show_balance()
                elif choice == 2:
                    app.withdraw()
                elif choice == 3:
                    app.deposit()
                elif choice == 4:
                    print("Thank you for using the Banking App. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please select an option from 1 to 4.\n")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.\n")


if __name__ == '__main__':
    app = BankingApp()
    app.run()
