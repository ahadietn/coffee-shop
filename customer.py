class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) < 1 or len(value) > 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        return self._orders.copy()

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        from coffee import Coffee
        from order import Order
        if not isinstance(coffee, Coffee):
            raise ValueError("Coffee must be a Coffee instance")
        if not isinstance(price, (int, float)) or price < 1.0 or price > 10.0:
            raise ValueError("Price must be a number between 1.0 and 10.0")
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee._orders.append(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise ValueError("Coffee must be a Coffee instance")

        customers = {}
        for order in coffee._orders:
            customer = order.customer
            if customer not in customers:
                customers[customer] = 0
            customers[customer] += order.price

        if not customers:
            return None

        return max(customers, key=customers.get)
