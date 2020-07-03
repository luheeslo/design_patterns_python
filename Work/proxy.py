from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):

    @abstractmethod
    def do_pay(self):
        pass


class Bank(Payment):

    """Docstring for Bank. """

    def __init__(self):
        self.card = None
        self.account = None

    def __getAccount(self):
        self.account = self.card
        return self.account

    def __hasFunds(self):
        """TODO: Docstring for _hasFunds.
        :returns: TODO

        """
        print("Bank:: Checking if Account", self.__getAccount(), "has enough funds")
        return False

    def setCard(self, card):
        """TODO: Docstring for setCard.

        :card: TODO
        :returns: TODO

        """
        self.card = card

    def do_pay(self):
        """TODO: Docstring for do_pay.
        :returns: TODO

        """
        if self.__hasFunds():
            print("Bank:: Paying the merchant")
            return True
        else:
            print("Bank:: Sorry, not enough funds")
            return False


class DebitCard(Payment):

    """Docstring for Bank. """

    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        """TODO: Docstring for do_pay.
        :returns: TODO

        """
        card = input("Proxy:: Punch in Card Number: ")
        self.bank.setCard(card)
        return self.bank.do_pay()


class You:

    """Docstr foou. """

    def __init__(self):
        print("You:: Lets buy the Denim shirt")
        self.debitCard = DebitCard()
        self.isPurchased = None

    def make_payment(self):
        """TODO: Docstring for make_payment.

        :f: TODO
        :returns: TODO

        """
        self.isPurchased = self.debitCard.do_pay()

    def __del__(self):
        """TODO: Docstring for __del__.
        :returns: TODO

        """
        if self.isPurchased:
            print("You:: Wow! Denim shirt is Mine :-)")
        else:
            print("You:: I should earn more :-(")


you = You()
you.make_payment()
