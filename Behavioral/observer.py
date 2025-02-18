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
        


# ---------  Challenge: Weather Station System ---------
"""
You need to create a weather station that broadcasts temperature updates to multiple devices. 
Devices like a Phone, Laptop, and Tablet should get updates when the weather changes.

✅ Your task:

    1- Implement the Observer Pattern:
        - Subject: WeatherStation – Keeps track of the temperature.
        - Observers: PhoneDisplay, LaptopDisplay, TabletDisplay – Receive and display temperature updates.
        
    2- Ensure that when the temperature changes, all devices receive the update.
    3- Add methods to register, remove, and notify devices.
"""


# Answer

class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        pass
    

class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer:Observer):
        pass
    
    @abstractmethod
    def remove_observer(self, observer:Observer):
        pass
    
    @abstractmethod
    def notify_observers(self):
        pass
    
class WeatherStation(Subject):
    
    def __init__(self):
        self._observers = []
        self._temperature = 0
        
        
    def register_observer(self, observer:Observer):
        self._observers.append(observer)
    
    
    def remove_observer(self, observer:Observer):
        self._observers.remove(observer)
    
    
    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)
            
    def set_temperature(self, temperature):
        self._temperature = temperature
        print(f"\nWeatherStation: Temperature updated to {temperature}°C")
        self.notify_observers()

class Device(Observer):
    def __init__(self, device):
        self.device = device
        
    def update(self, temperature):
        print(f"{self.device} received update: The new temperature is {temperature}°C")
            
        
station = WeatherStation()

device1 = Device("PhoneDisplay")
device2 = Device("LaptopDisplay")
device3 = Device("TabletDisplay")

station.register_observer(device1)
station.register_observer(device2)
station.register_observer(device3)


station.remove_observer(device2)

station.set_temperature(120)
station.set_temperature(-250)