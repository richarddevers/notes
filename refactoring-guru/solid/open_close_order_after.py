import abc


class Shipping(abc.ABC):
    @abc.abstractmethod
    def get_cost(self, order: "Order") -> int:
        raise NotImplementedError()


class Ground(Shipping):
    def get_cost(self, order: "Order") -> int:
        if order.get_total() > 100:
            return 0
        return 2 * order.get_total_weight()


class Air(Shipping):
    def get_cost(self, order: "Order") -> int:
        return 3 * order.get_total_weight()


class Order:
    linetItems: str
    shipping: Shipping

    def get_total(self) -> int:
        return 101

    def get_total_weight(self) -> int:
        return 102

    def get_shipping_cost(self):
        return self.shipping.get_cost(order=self)

    def get_shipping_date(self):
        pass


new_order = Order()
new_order.shipping = Ground()
cost = new_order.get_shipping_cost()
