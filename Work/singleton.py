"""
File: singleton.py
Author: luheeslo
Email: luheeslo@email.com
Github: https://github.com/luheeslo
Description: Single pattern example.
"""


class Singleton:  # pylint: disable=too-few-public-methods

    """This class is responsible for create one and only one object
    of the class gets created.
    """

    def __new__(cls):
        """TODO: Docstring for __new__.

        :cls: TODO
        :returns: TODO

        """
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


class SingleLazy:  # pylint: disable=too-few-public-methods

    """Docstring for SingleLazy. """

    __instance = None

    def __init__(self):
        """TODO: to be defined. """
        if not SingleLazy.__instance:
            print("__init__ method called..")
        else:
            print("Instance already created: ", self.get_instance())

    @classmethod
    def get_instance(cls):
        """teste1"""
        if not cls.__instance:
            cls.__instance = SingleLazy()
        return cls.__instance
