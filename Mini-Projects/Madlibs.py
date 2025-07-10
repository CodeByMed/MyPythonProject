"""Madlibs Game"""
def madlibs() -> None:
    """Main function for the Madlibs Game"""
    try:
        noun = input("Enter a noun (e.g., table, house): ").strip()
        verb = input("Enter a verb (e.g., walked, ate): ").strip()
        adjective = input("Enter an adjective (e.g., ugly, pretty): ").strip()

        # Validate that inputs are not digits or empty
        if not noun.isalpha() or not verb.isalpha() or not adjective.isalpha():
            raise ValueError("All inputs must be alphabetic words without numbers or special characters.")

        # Capitalize only for output (not during input parsing)
        print(f"\nToday, me and my {noun.capitalize()} {verb.lower()}, and we saw a car that looked very {adjective.lower()}.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    madlibs() # Run the Application.
