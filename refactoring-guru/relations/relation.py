class RiceCooker:
    button: bool


class Chef:
    @staticmethod
    def cook_rice():
        RiceCooker.button = True


# Chef interact with RiceCooker
