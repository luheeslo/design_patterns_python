"""
File: monostate.py
Author: yourname
Email: yourname@email.com
Github: https://github.com/yourname
Description: Monostate pattern example.
"""


class Borg:  # pylint: disable=too-few-public-methods

    """Docstring for Borg. """

    __shared_state = {"1": "2"}

    def __init__(self):
        """TODO: Docstring for __init__.
        :returns: TODO

        """
        self._x = 1
        self.__dict__ = self.__shared_state


B = Borg()
B1 = Borg()

print("Borg object: 'B': ", B)
print("Borg object: 'B1': ", B1)
print("Object State: 'B': ", id(B.__dict__))
print("Object State: 'B1': ", id(B1.__dict__))
