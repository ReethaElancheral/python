# 7. Restaurant Billing System

# Concepts: Composition, Class Variables, Static Methods
# Classes:  MenuItem,  Order, Bill, Customer
# Requirements:
# Add/remove menu items
# Place order and generate bill with taxes
# Use class variable for global tax rate

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price  # INR

    def __str__(self):
        return f"{self.name}: ₹{self.price}"


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, menu_item):
        self.items.append(menu_item)
        print(f"Added {menu_item.name} to order.")

    def remove_item(self, menu_item):
        if menu_item in self.items:
            self.items.remove(menu_item)
            print(f"Removed {menu_item.name} from order.")
        else:
            print(f"{menu_item.name} not in order.")

    def total_price(self):
        return sum(item.price for item in self.items)


class Bill:
    tax_rate = 5  # 5% global tax rate, class variable

    def __init__(self, order):
        self.order = order

    def calculate_tax(self):
        return self.order.total_price() * Bill.tax_rate / 100

    def total_amount(self):
        return self.order.total_price() + self.calculate_tax()

    @staticmethod
    def print_tax_info():
        print(f"Current tax rate is {Bill.tax_rate}%.")

    def generate_bill(self):
        print(f"Bill for {self.order.customer.name}:")
        for item in self.order.items:
            print(f" - {item}")
        print(f"Subtotal: ₹{self.order.total_price():.2f}")
        tax = self.calculate_tax()
        print(f"Tax (@{Bill.tax_rate}%): ₹{tax:.2f}")
        print(f"Total: ₹{self.total_amount():.2f}")


class Customer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Customer: {self.name}"


def main():
    # Create customer
    customer = Customer("Nisha")

    # Create menu items
    pizza = MenuItem("Pizza", 300)
    burger = MenuItem("Burger", 150)
    soda = MenuItem("Soda", 50)

    # Create order
    order = Order(customer)
    order.add_item(pizza)
    order.add_item(burger)
    order.add_item(soda)

    # Remove an item
    order.remove_item(soda)

    # Show tax info
    Bill.print_tax_info()

    # Generate bill
    bill = Bill(order)
    bill.generate_bill()


if __name__ == "__main__":
    main()
