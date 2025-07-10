'''Temperature Conversion Program'''
class TemperatureConversion:
    def convert_c_to_f(self, celsius: float) -> float:
        """Convert Celsius to Fahrenheit"""
        return (celsius * 9 / 5) + 32

    def convert_f_to_c(self, fahrenheit: float) -> float:
        """Convert Fahrenheit to Celsius"""
        return (fahrenheit - 32) * 5 / 9

    def get_unit_input(self) -> str:
        unit = input("Convert from Celsius (C) or Fahrenheit (F)? ").strip().upper()
        if unit not in ('C', 'F'):
            raise ValueError("Invalid unit. Use 'C' or 'F'.")
        return unit

    def get_temperature_input(self) -> float:
        try:
            return float(input("Enter the temperature to convert: "))
        except ValueError as e:
            raise ValueError("Invalid input. Must be a number.") from e

    def run(self):
        try:
            unit = self.get_unit_input()
            temp = self.get_temperature_input()

            if unit == 'C':
                result = self.convert_c_to_f(temp)
                print(f"{temp}°C is {result:.2f}°F")
            else:
                result = self.convert_f_to_c(temp)
                print(f"{temp}°F is {result:.2f}°C")

        except ValueError as err:
            print(err)

if __name__ == '__main__':
    app = TemperatureConversion()
    app.run()
