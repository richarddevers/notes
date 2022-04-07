class RiceCooker:
    @staticmethod
    def heat():
        print("heating...")


class Chef(RiceCooker):
    pass


Chef.heat()

# Chef inherit of RiceCooker
# it can now use the inherited heat() method
