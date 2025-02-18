from abc import ABC, abstractmethod


# --------- Challenge: Vehicle Factory ---------

"""
Create a Vehicle Factory that produces different types of vehicles. 
Each vehicle should have specific properties and behaviors.

📋 Requirements:
1- Abstract Class:

    Vehicle (with an abstract method specifications()).

2- Subclasses:
    Implement the following vehicle types:

    Car – Prints: "Car: 4 wheels, max speed 200 km/h"
    Bike – Prints: "Bike: 2 wheels, max speed 100 km/h"
    Truck – Prints: "Truck: 6 wheels, max speed 120 km/h"
    Vehicle Factory:

3- VehicleFactory should return the correct vehicle object:

    "car" → Car
    "bike" → Bike
    "truck" → Truck

4- Bonus (Optional but Fun!):

    If an unknown vehicle type is requested, raise an error message: "Unknown vehicle type: {type}".
"""

# Answer
class Vehicle(ABC):
   
    @abstractmethod
    def specification(self):
        pass
    

class Car(Vehicle):
    def specification(self):
        print(f"Car: 4 wheels, max speed 250 km/h")
    
    
class Bike(Vehicle):
    def specification(self):
        print(f"Bike: 2 wheels, max speed 100 km/h")


class Truck(Vehicle):
    def specification(self):
        print(f"Truck: 6 wheels, max speed 120 km/h")



class VehicleFactory:
    def create_vehicle(self, vehicle):
        vehicles = {
            'car': Car,
            'bike': Bike,
            'truck': Truck,
        }
        if vehicle not in vehicles:
            raise ValueError(f"Unknown vehicle type: {vehicle}")
            
        else:
            return vehicles[vehicle]()
        

# --------- Challenge: Smart Home Device Factory ---------
"""
You will create a Smart Home Factory that produces different types of smart devices. 
Each device will have unique actions it can perform.

📋 Requirements:
1- Abstract Class:

    SmartDevice with two abstract methods:
    turn_on()
    turn_off()
    
2- Subclasses (Concrete Devices):

    SmartLight:
    turn_on() → "Smart Light is ON"
    turn_off() → "Smart Light is OFF"
    SmartThermostat:
    turn_on() → "Thermostat set to 22°C"
    turn_off() → "Thermostat turned OFF"
    SmartDoorLock:
    turn_on() → "Door is LOCKED"
    turn_off() → "Door is UNLOCKED"
    
3- Factory Class:

    SmartDeviceFactory should create devices based on the following input:
    "light" → SmartLight
    "thermostat" → SmartThermostat
    "doorlock" → SmartDoorLock
    If the device type is unknown, raise a ValueError with the message:
    "Unknown device type: {device}"
    
4- Bonus Challenge (Optional but Fun!):

    Add a status attribute to track whether the device is currently ON or OFF.
    Create a get_status() method to report the device's current state.
"""


# Asnwer
class SmartDevice(ABC):
    
    def __init__(self):
        self.status = False
    
    @abstractmethod
    def turn_on(self): pass
    
    @abstractmethod
    def turn_off(self): pass
    
    @abstractmethod
    def get_status(self):
        pass
    

class SmartLight(SmartDevice):
    def turn_on(self):
        self.status = True
        print("Smart Light is ON")
    
    def turn_off(self):
        self.status = False
        print("Smart Light is OFF")
        
    def get_status(self):
        return f"Smart Light Status is {self.status}"
        
        
class SmartThermostat(SmartDevice):
    def turn_on(self):
        self.status = True
        print("Smart Thermostat is ON")
    
    def turn_off(self):
        self.status = False
        print("Smart Thermostat is OFF")
        
    def get_status(self):
        return f"Smart Thermostat Status is {self.status}"
        
        
class SmartDoorLock(SmartDevice):
    def turn_on(self):
        self.status = True
        print("Smart DoorLock is ON")
    
    def turn_off(self):
        self.status = False
        print("Smart DoorLock is OFF")
        
    def get_status(self):
        return f"Smart DoorLock Status is {self.status}"
        

class SmartDeviceFactory:
    def create_device(self, device):
        devices = {
            "light" : SmartLight,
            "thermostat" : SmartThermostat,
            "doorlock" : SmartDoorLock,
        }
        
        if device not in devices:
            raise ValueError(f"Unknown device type: {device}")
        
        else:
            return devices[device]()
        