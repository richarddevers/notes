# initial


class Cat:
    pass


class A:
    def buy_cat(self) -> Cat:
        return Cat()


# good
class Cat2:
    pass


class BengualCat(Cat2):
    pass


class A2:
    def buy_cat(self) -> Cat2:
        return Cat2()


class B(A2):
    def buy_cat(self) -> BengualCat:
        return BengualCat()


# bad


class Animal:
    pass

class Cat3(Animal):
    pass

class A3:
    def buy_cat(self) -> Cat:
        return Cat()


class B3(A3):
    def buy_cat(self) -> Animal:
        return Animal()
