import pytest
from coffee import Coffee
from customer import Customer

class TestCoffee:
    def test_coffee_init_valid_name(self):
        coffee = Coffee("Latte")
        assert coffee.name == "Latte"

    def test_coffee_init_invalid_name_type(self):
        with pytest.raises(ValueError, match="Name must be a string"):
            Coffee(123)

    def test_coffee_init_name_too_short(self):
        with pytest.raises(ValueError, match="Name must be at least 3 characters long"):
            Coffee("Hi")

    def test_coffee_orders_empty(self):
        coffee = Coffee("Latte")
        assert coffee.orders() == []

    def test_coffee_customers_empty(self):
        coffee = Coffee("Latte")
        assert coffee.customers() == []

    def test_coffee_num_orders_empty(self):
        coffee = Coffee("Latte")
        assert coffee.num_orders() == 0

    def test_coffee_average_price_empty(self):
        coffee = Coffee("Latte")
        assert coffee.average_price() == 0.0

    def test_coffee_orders_with_data(self):
        coffee = Coffee("Latte")
        customer = Customer("Alice")
        customer.create_order(coffee, 5.0)
        customer.create_order(coffee, 3.0)

        assert len(coffee.orders()) == 2
        assert coffee.num_orders() == 2
        assert coffee.average_price() == 4.0

    def test_coffee_customers_unique(self):
        coffee = Coffee("Latte")
        alice = Customer("Alice")
        bob = Customer("Bob")

        alice.create_order(coffee, 5.0)
        bob.create_order(coffee, 3.0)
        alice.create_order(coffee, 4.0)

        customers = coffee.customers()
        assert len(customers) == 2
        assert alice in customers
        assert bob in customers
