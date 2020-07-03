class EventManager:

    def __init__(self):
        """TODO: Docstring for __init__.
        :returns: TODO

        """
        print("Event Manager:: Let me talk to the folks\n")

    def arrange(self):
        """TODO: Docstring for arrange.
        :returns: TODO

        """
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()

        self.florist = Florist()
        self.florist.setFlowerRequirements()

        self.caterer = Caterer()
        self.caterer.setCuisine()

        self.musician = Musician()
        self.musician.setMusicType()


class Hotelier:  # pylint: disable=too-few-public-methods

    def __init__(self):
        """TODO: Docstring for __init__.
        :returns: TODO

        """
        print("Arraging the Hotel for Marriage? --")

    def __isAvailable(self):
        """TODO: Docstring for __isAvailable.
        :returns: TODO

        """
        print("Is the Hotel free for the event on given day?")
        return True

    def bookHotel(self):
        if self.__isAvailable():
            print("Registered the Booking\n\n")


class Florist:
    def __init__(self):
        """TODO: Docstring for __init__.
        :returns: TODO

        """
        print("Flower decorations for the Event? --")

    def setFlowerRequirements(self):
        """TODO: Docstring for setFlowerRequirements.
        :returns: TODO

        """
        print("Carnations, Roses and Lilies would be used for Decorations\n\n")


class Caterer:
    def __init__(self):
        """TODO: Docstring for __init__.
        :returns: TODO

        """
        print("Food Arrangements for the Event --")

    def setCuisine(self):
        """TODO: Docstring for setCuisine.
        :returns: TODO

        """
        print("Chinese & Continental Cuisine to be served\n\n")


class Musician:
    def __init__(self):
        """TODO: Docstring for __init__.
        :returns: TODO

        """
        print("Musical Arrangements for the Marriage --")

    def setMusicType(self):
        """TODO: Docstring for setMusicType.
        :returns: TODO

        """
        print("Jazz and Classical will be played\n\n")


class You:
    def __init__(self):
        """TODO: Docstring for __init__.
        :returns: TODO

        """
        print("You:: Whoa! Marriage Arrangements??!!")

    def askEventManager(self):
        """TODO: Docstring for askEventManager.
        :returns: TODO

        """
        print("You:: Let's Contact the Evenet Manager\n\n")
        em = EventManager()
        em.arrange()


if __name__ == "__main__":
    You().askEventManager()
