class Order:
    linetItems: str
    shipping: str

    def get_total(self) -> int:
        return 101  # ...

    def get_total_weight(self) -> int:
        return 102  # ...

    def get_shipping_cost(self):
        if self.shipping == "ground":
            if self.get_total() > 100:
                return 0
            return 2 * self.get_total_weight()

        if self.shipping == "air":
            return 3 * self.get_total_weight()

    def get_shipping_date(self):
        pass


new_order = Order()
new_order.shipping = "ground"
cost = new_order.get_shipping_cost()
