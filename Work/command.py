# Abstract Command
class Order:

    def execute(self):
        raise NotImplementedError


# Concrete Command
class BuyStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()


# Concrete Command
class SellStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()

# Receiver
class StockTrade:
    def buy(self):
        print("You will buy stocks.")

    def sell(self):
        print("You will sell stocks.")


# Invoker
class Agent:
    def __init__(self):
        self.__orderQueue = []

    def placeOrder(self, order):
        self.__orderQueue.append(order)
        order.execute()


if __name__ == "__main__":
    stock = StockTrade()
    buyStock = BuyStockOrder(stock)
    sellStock = SellStockOrder(stock)

    agent = Agent()
    agent.placeOrder(buyStock)
    agent.placeOrder(sellStock)
