import pytest
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder:
    def test_order_init_valid(self):
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 5.0)

        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 5.0

    def test_order_init_invalid_customer(self):
        coffee = Coffee("Latte")
        with pytest.raises(ValueError, match="Customer must be a Customer instance"):
            Order("Alice", coffee, 5.0)

    def test_order_init_invalid_coffee(self):
        customer = Customer("Alice")
        with pytest.raises(ValueError, match="Coffee must be a Coffee instance"):
            Order(customer, "Latte", 5.0)

    def test_order_init_invalid_price_type(self):
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        with pytest.raises(ValueError, match="Price must be a number"):
            Order(customer, coffee, "5.0")

    def test_order_init_price_too_low(self):
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        with pytest.raises(ValueError, match="Price must be between 1.0 and 10.0"):
            Order(customer, coffee, 0.5)

    def test_order_init_price_too_high(self):
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        with pytest.raises(ValueError, match="Price must be between 1.0 and 10.0"):
            Order(customer, coffee, 15.0)

    def test_order_price_conversion(self):
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 5)
        assert order.price == 5.0
        assert isinstance(order.price, float)
