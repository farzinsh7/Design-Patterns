from abc import ABC, abstractmethod
# ---------  Challenge: Build a Stock Price Notifier ---------
"""
Imagine you are building a system where different users (observers) want to track the price of a stock. 
Whenever the stock price changes, all registered users should be notified.

✅ Your Task:
    1- Create a Stock (the subject) that:

        - Holds the stock price.
        - Allows users to register and unregister.
        - Notifies all users when the price changes.
        
    2- Create Users (observers) that:

        - Receive updates when the stock price changes.
        - Display the updated stock price.
"""


# Answer
class Observer(ABC):
    @abstractmethod
    def update(self, price):
        pass
    

class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer):
        pass
    
    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass
    
    @abstractmethod
    def notify_observers(self):
        pass
    
    
class Stock(Subject):
    def __init__(self):
        self._observers = []
        self._price = 0
    
    def register_observer(self, observer: Observer):
        self._observers.append(observer)
    

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)
    

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._price)
            
    def set_price(self, price):
        self._price = price
        self.notify_observers()


class User(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, price):
        print(f"{self.name} received update: The new stock price is ${price}")
        

stock = Stock()

user1 = User("Alice")
user2 = User("Bob")

stock.register_observer(user1)
stock.register_observer(user2)

stock.set_price(100)

