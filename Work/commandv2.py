# Command
def buy_stock_order(stock):
    stock.buy()


# Command
def sell_stock_order(stock):
    stock.sell()


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

    def placeOrder(self, stock, order):
        self.__orderQueue.append(order)
        order(stock)


if __name__ == "__main__":
    stock = StockTrade()
    agent = Agent()
    agent.placeOrder(stock, buy_stock_order)
    agent.placeOrder(stock, sell_stock_order)
