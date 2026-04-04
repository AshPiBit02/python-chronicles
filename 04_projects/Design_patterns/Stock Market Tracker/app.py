# Subject
class StockFeed:
    def __init__(self):
        self._obervers=[]
        self._prices={}
    def attach(self,observer):
        self._obervers.append(observer)
    def detach(self,observer):
        self._obervers.remove(observer)
    def set_price(self,stock,price):
        self._prices[stock] = price
        self.broadcast(stock,price)
    def broadcast(self,stock,price):
        for observer in self._obervers:
            observer.update(stock,price)

# Observer Interface
class Observer:
    def update(self,stock,price): pass

# Concrete Observers
class mblAppObserver(Observer):
    def update(self,stock,price):
        print(f"[Mobile App] {stock} updated to {price}$")
class webDashboardObserver(Observer):
    def update(self,stock,price):
        print(f"[Dashboard] Refresh chart:{stock} = {price}$")
class tradingBotObserver(Observer):
    def update(self,stock,price):
        if price>1000:
            print(f"[Trading Bot] SELL {stock} at {price}$")
        else:
            print(f"[Trading Bot] BUY {stock} at {price}$")

