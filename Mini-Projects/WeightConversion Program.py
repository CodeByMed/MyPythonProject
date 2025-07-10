'''Weight Conversion Program'''
class ConversionProgram:
    def app(self): # Main Entry Point
        # Unit: Kilogramm (K) or Pound (L)
        unit = input("Which unit to use? 'K' for Kilograms or 'L' for Pounds: ").strip().upper()

        try:
            weight = float(input("Enter the weight to convert: ")) # Get the Weight
        except ValueError:
            print("Please enter a valid numeric value.")
            return

        '''--- Converting Part ---'''
        if unit == "K":
            converted = weight * 2.20462  # kg -> lbs
            print(f"{weight} Kilograms is {converted:.2f} Pounds.")
        elif unit == "L":
            converted = weight / 2.20462  # lbs -> kg
            print(f"{weight} Pounds is {converted:.2f} Kilograms.")
        else:
            print("Invalid unit. Please enter 'K' or 'L'.")

if __name__ == '__main__':
    '''Initialize the Class Variable'''
    WeightConversion = ConversionProgram()
    WeightConversion.app() # Run the Main Application.
