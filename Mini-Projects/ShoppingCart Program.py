class ShoppingCart:
    """
    A simple shopping cart that lets users input food items with price and quantity,
    then displays a summary of the cart with total cost.
    """
    def __init__(self):
        self.food_items = []

    def add_item(self):
        """Prompts the user to add an item to the cart."""
        try:
            food = input("Enter food to add (q to quit): ").strip()
            if food.lower() == 'q':
                return False

            price = float(input("Enter price per item: "))
            quantity = int(input("Enter quantity: "))
            total = price * quantity

            self.food_items.append({
                'name': food.capitalize(),
                'price': price,
                'quantity': quantity,
                'total': total
            })

            return True

        except ValueError:
            print("Invalid input. Price must be a number and quantity must be an integer.")
            return True

    def run(self):
        """Runs the shopping cart program loop."""
        print("🛒 Welcome to the Shopping Cart Program!")
        try:
            while self.add_item():
                pass
        except KeyboardInterrupt:
            print("\nProgram interrupted.")

        self.print_summary()

    def print_summary(self):
        """Displays the cart summary and total cost."""
        print("\n🧾 Cart Summary:")
        if not self.food_items:
            print("No items in the cart.")
            return

        grand_total = 0
        for item in self.food_items:
            print(f"- {item['quantity']}x {item['name']} @ {item['price']:.2f} each = {item['total']:.2f}")
            grand_total += item['total']

        print(f"\n💰 Total cost: {grand_total:.2f} EUR")


if __name__ == "__main__":
    App = ShoppingCart()
    App.run()
