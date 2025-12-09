#!/usr/bin/env python3

from customer import Customer
from coffee import Coffee
from order import Order

def test_basic_functionality():
    print("=== Testing Basic Functionality ===")

    # Create customers
    alice = Customer("Alice")
    bob = Customer("Bob")
    charlie = Customer("Charlie")

    print(f"Created customers: {alice.name}, {bob.name}, {charlie.name}")

    # Create coffees
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")
    cappuccino = Coffee("Cappuccino")

    print(f"Created coffees: {latte.name}, {espresso.name}, {cappuccino.name}")

    # Create orders
    order1 = alice.create_order(latte, 5.0)
    order2 = alice.create_order(espresso, 3.0)
    order3 = bob.create_order(latte, 4.5)
    order4 = charlie.create_order(cappuccino, 6.0)
    order5 = alice.create_order(latte, 5.5)

    print(f"Created {len([order1, order2, order3, order4, order5])} orders")

    # Test relationships
    print("\n=== Testing Relationships ===")
    print(f"Alice's orders: {len(alice.orders())}")
    print(f"Alice's coffees: {[coffee.name for coffee in alice.coffees()]}")

    print(f"Latte's orders: {latte.num_orders()}")
    print(f"Latte's average price: ${latte.average_price():.2f}")
    print(f"Latte's customers: {[customer.name for customer in latte.customers()]}")

    # Test most_aficionado
    print(f"\nMost aficionado of Latte: {Customer.most_aficionado(latte).name}")

def test_error_handling():
    print("\n=== Testing Error Handling ===")

    try:
        Customer("")  # Invalid name
    except ValueError as e:
        print(f"✓ Caught expected error: {e}")

    try:
        Coffee("Hi")  # Name too short
    except ValueError as e:
        print(f"✓ Caught expected error: {e}")

    try:
        customer = Customer("Test")
        coffee = Coffee("Test")
        Order(customer, coffee, 15.0)  # Price too high
    except ValueError as e:
        print(f"✓ Caught expected error: {e}")

if __name__ == "__main__":
    test_basic_functionality()
    test_error_handling()
    print("\n=== All tests completed ===")
