class RiceCooker:
    button: bool


class Chef:
    rice_cooker: RiceCooker

    def __init__(self) -> None:
        self.rice_cooker = RiceCooker()


# Chef knows about RiceCooker and consit of RiceCooker
# It manage his lifecycle
# RiceCooker should not lived outside the Chef class
