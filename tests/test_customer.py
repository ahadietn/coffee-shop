import pytest
from customer import Customer
from coffee import Coffee

class TestCustomer:
    def test_customer_init_valid_name(self):
        customer = Customer("Alice")
        assert customer.name == "Alice"

    def test_customer_init_invalid_name_type(self):
        with pytest.raises(ValueError, match="Name must be a string"):
            Customer(123)

    def test_customer_init_name_too_short(self):
        with pytest.raises(ValueError, match="Name must be between 1 and 15 characters"):
            Customer("")

    def test_customer_init_name_too_long(self):
        with pytest.raises(ValueError, match="Name must be between 1 and 15 characters"):
            Customer("A" * 16)

    def test_customer_orders_empty(self):
        customer = Customer("Alice")
        assert customer.orders() == []

    def test_customer_coffees_empty(self):
        customer = Customer("Alice")
        assert customer.coffees() == []

    def test_customer_create_order_valid(self):
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        order = customer.create_order(coffee, 5.0)
        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 5.0
        assert order in customer.orders()
        assert order in coffee.orders()

    def test_customer_create_order_invalid_coffee(self):
        customer = Customer("Alice")
        with pytest.raises(ValueError, match="Coffee must be a Coffee instance"):
            customer.create_order("Latte", 5.0)

    def test_customer_create_order_invalid_price(self):
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        with pytest.raises(ValueError, match="Price must be a number between 1.0 and 10.0"):
            customer.create_order(coffee, 15.0)

    def test_customer_most_aficionado(self):
        coffee = Coffee("Latte")
        alice = Customer("Alice")
        bob = Customer("Bob")

        alice.create_order(coffee, 5.0)
        alice.create_order(coffee, 3.0)
        bob.create_order(coffee, 4.0)

        assert Customer.most_aficionado(coffee) == alice

    def test_customer_most_aficionado_no_orders(self):
        coffee = Coffee("Latte")
        assert Customer.most_aficionado(coffee) is None

    def test_customer_most_aficionado_invalid_coffee(self):
        with pytest.raises(ValueError, match="Coffee must be a Coffee instance"):
            Customer.most_aficionado("Latte")
