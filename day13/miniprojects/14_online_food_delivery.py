# 14. Online Food Delivery

# Concepts: Inheritance, Aggregation, Polymorphism
# Classes:  User, Customer,  Restaurant,  Order, Delivery
# Requirements:
# Place order, assign delivery agent
# Use polymorphism for delivery type
# Aggregate restaurant in order

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def get_role(self):
        return "User"

class Customer(User):
    def __init__(self, user_id, name, address):
        super().__init__(user_id, name)
        self.address = address

    def get_role(self):
        return "Customer"

class Restaurant:
    def __init__(self, restaurant_id, name):
        self.restaurant_id = restaurant_id
        self.name = name
        self.menu = {}

    def add_menu_item(self, item_name, price):
        self.menu[item_name] = price

    def __str__(self):
        return f"Restaurant: {self.name}"

class Delivery:
    def __init__(self, delivery_id, agent_name):
        self.delivery_id = delivery_id
        self.agent_name = agent_name

    def deliver(self):
        raise NotImplementedError("Subclasses must implement deliver method")

class HomeDelivery(Delivery):
    def deliver(self):
        print(f"Home delivery by {self.agent_name}")

class PickupDelivery(Delivery):
    def deliver(self):
        print(f"Pickup delivery by {self.agent_name}")

class Order:
    order_counter = 0

    def __init__(self, customer, restaurant):
        self.order_id = Order.order_counter + 1
        Order.order_counter = self.order_id
        self.customer = customer
        self.restaurant = restaurant  # aggregation
        self.items = []
        self.delivery_agent = None

    def add_item(self, item_name):
        if item_name in self.restaurant.menu:
            self.items.append(item_name)
            print(f"Added {item_name} to order.")
        else:
            print(f"Item {item_name} not available at {self.restaurant.name}")

    def assign_delivery_agent(self, delivery_agent):
        self.delivery_agent = delivery_agent
        print(f"Assigned delivery agent: {delivery_agent.agent_name}")

    def deliver_order(self):
        if self.delivery_agent:
            print(f"Delivering order {self.order_id} for {self.customer.name}")
            self.delivery_agent.deliver()
        else:
            print("No delivery agent assigned.")

    def __str__(self):
        return (f"Order ID: {self.order_id}\n"
                f"Customer: {self.customer.name}\n"
                f"Restaurant: {self.restaurant.name}\n"
                f"Items: {', '.join(self.items)}")

def main():
    # Create customer
    customer = Customer(1, "Nisha", "123, Some Street")

    # Create restaurant and add menu items
    restaurant = Restaurant(101, "Tasty Bites")
    restaurant.add_menu_item("Burger", 150)
    restaurant.add_menu_item("Pizza", 300)
    restaurant.add_menu_item("Pasta", 250)

    # Create order
    order = Order(customer, restaurant)
    order.add_item("Pizza")
    order.add_item("Burger")

    # Assign delivery agent
    delivery_agent = HomeDelivery(201, "Ravi")
    order.assign_delivery_agent(delivery_agent)

    # Print order details and deliver
    print(order)
    order.deliver_order()

    # Try pickup delivery example
    pickup_agent = PickupDelivery(202, "Anita")
    order.assign_delivery_agent(pickup_agent)
    order.deliver_order()

if __name__ == "__main__":
    main()
