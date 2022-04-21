# intial:


class Cat1:
    pass


class A1:
    def feed(self, animal: Cat1):
        pass


# good:


class Animal2:
    pass


class Cat2(Animal2):
    pass


class A2:
    def feed(self, animal: Cat2):
        pass


class B(A2):
    def feed(self, animal: Animal2)  # the cat has been abstract into an animal
        pass


# bad:

class Cat3:
    pass


class CatBengual:
    pass


class A3:
    def feed(self, animal: Cat3):
        pass

class C:
    def feed(
        self, cat_bengual: CatBengual
    ):  # the parameter type changed, more specialization there's no genericity
        pass
