import abc


class HeatingCookingTool(abc.ABC):
    @abc.abstractstaticmethod
    def heat() -> None:
        raise NotImplementedError()


class RiceCooker(HeatingCookingTool):
    @staticmethod
    def heat() -> None:
        print("heating...")


# RiceCooker implements HeatingCookingTool abstract class (an interface like)
# it has to implment the heat() method
