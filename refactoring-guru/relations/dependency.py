class RiceCooker:
    @staticmethod
    def heat():
        print("heating...")


class Chef:
    @staticmethod
    def cook_rice():
        # ...
        RiceCooker.heat()


# Chef depends on RiceCooker
# if heat() change (new param?), Chef will break
