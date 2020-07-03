from abc import ABCMeta, abstractmethod


class PizzaFactory(metaclass=ABCMeta):  # pylint: disable=too-few-public-methods
    """docstring for PizzaFactory"""

    @abstractmethod
    def create_veg_pizza(self):
        """TODO: Docstring for createVegPizza.
        :returns: TODO

        """
        pass

    @abstractmethod
    def create_non_veg_pizza(self):
        """TODO: Docstring for createNonVegPizza.
        :returns: TODO

        """
        pass


class IndianPizzaFactory(PizzaFactory):  # pylint: disable=too-few-public-methods
    """docstring for IndianPizzaFactory"""

    def create_veg_pizza(self):
        """TODO: Docstring for create_veg_pizza.
        :returns: TODO

        """
        return DeluxVeggiePizza()

    def create_non_veg_pizza(self):
        """TODO: Docstring for create_veg_pizza.
        :returns: TODO

        """
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):  # pylint: disable=too-few-public-methods
    """docstring for USPizzaFactory"""

    def create_veg_pizza(self):
        """TODO: Docstring for create_veg_pizza.
        :returns: TODO

        """
        return MexicanVegPizza()

    def create_non_veg_pizza(self):
        """TODO: Docstring for create_veg_pizza.
        :returns: TODO

        """
        return HamPizza()


class VegPizza(metaclass=ABCMeta):  # pylint: disable=too-few-public-methods
    """docstring for VegPizza"""
    @abstractmethod
    def prepare(self):
        """TODO: Docstring for prepare.
        :returns: TODO

        """
        pass


class NonVegPizza(metaclass=ABCMeta):  # pylint: disable=too-few-public-methods
    """docstring for VegPizza"""
    @abstractmethod
    def serve(self, veg_pizza):
        """TODO: Docstring for prepare.

        :VegPizza: TODO
        :returns: TODO

        """
        pass


class DeluxVeggiePizza(VegPizza):  # pylint: disable=too-few-public-methods
    """docstring for DeluxVeggiePizza"""
    def prepare(self):
        """TODO: Docstring for prepare.
        :returns: TODO

        """
        print("Prepare ", type(self).__name__)


class ChickenPizza(NonVegPizza):  # pylint: disable=too-few-public-methods
    """docstring for ChickenPizza"""
    def serve(self, veg_pizza):
        """TODO: Docstring for serve.

        :VegPizza: TODO
        :returns: TODO

        """
        print(type(self).__name__, "is served with Chicken on ", type(veg_pizza).__name__)


class MexicanVegPizza(VegPizza):  # pylint: disable=too-few-public-methods
    """docstring for MexicanVegPizza"""
    def prepare(self):
        """TODO: Docstring for prepare.
        :returns: TODO

        """
        print("Prepare ", type(self).__name__)


class HamPizza(NonVegPizza):  # pylint: disable=too-few-public-methods
    """docstring for ChickenPizza"""
    def serve(self, veg_pizza):
        """TODO: Docstring for serve.

        :VegPizza: TODO
        :returns: TODO

        """
        print(type(self).__name__, "is served with Ham on ", type(veg_pizza).__name__)


class PizzaStore:  # pylint: disable=too-few-public-methods
    """docstring for PizzaStore"""
    def __init__(self):
        pass

    def make_pizzas(self):
        """TODO: Docstring for make_pizzas.

        :returns: TODO

        """
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.non_veg_pizza = self.factory.create_non_veg_pizza()
            self.veg_pizza = self.factory.create_veg_pizza()
            self.veg_pizza.prepare()
            self.non_veg_pizza.serve(self.veg_pizza)


if __name__ == "__main__":
    pizza = PizzaStore()
    pizza.make_pizzas()
