'''Calculator Program Python'''
class Calculator: # Class Calculator
    def app(self): # Main Entry Point
        operator = input("Enter an Operator (+, -, *, /): ") # Get Operator
        try:
            num1 = float(input("Enter number 1: ")) # Number 1
            num2 = float(input("Enter number 2: ")) # Number 2
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return # Returns nothing if that Happens.

        '''Check The Using Operator'''
        if operator == "+":
            result: float = num1 + num2
        elif operator == "-":
            result: float = num1 - num2
        elif operator == "*":
            result: float = num1 * num2
        elif operator == "/":
            try:
                result = num1 / num2
            except ZeroDivisionError: # Handling Zero Division Error (Can't Divide By Zero)
                print("You can't divide by zero!")
                return
        else:
            print(f"'{operator}' is not a valid operator.")
            return

        '''Show's The Result'''
        print(f"Result: {round(result, 2)}")

if __name__ == '__main__':
    calc = Calculator() # Initialize Variable
    calc.app() # Runs The Program
