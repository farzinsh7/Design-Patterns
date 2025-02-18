from abc import ABC, abstractmethod

# --------- Challenge: Pizza Shop ---------
"""
Imagine you're building a Pizza Shop where customers can customize their pizza. 
You have a base pizza (which is just a plain pizza) and various toppings that can be added, 
such as cheese, olives, mushrooms, and pepperoni.

    - The base pizza costs $8.
    - Each topping (cheese, olives, mushrooms, and pepperoni) costs $1 each.
    
Create a Pizza class with a cost and get_description method, then add the following toppings as decorators:

    - Cheese topping
    - Olives topping
    - Mushrooms topping
    - Pepperoni topping
    
Finally, create a pizza with all of the toppings and print both the cost and description.

Instructions:
    1- Define a Pizza base class.
    2- Create decorators for each topping (Cheese, Olives, Mushrooms, and Pepperoni).
    3- Use decorators to build a pizza with multiple toppings.
    4- Print the final cost and description.
"""


# Answer

class Pizza(ABC):
    @abstractmethod
    def cost(self):
        pass
    
    @abstractmethod
    def get_description(self):
        pass
    
class BasePizza(Pizza):

    def cost(self):
        return 10
    

    def get_description(self):
        return "Pizza"
    

class PizzaDeccorator(Pizza):
    def __init__(self, pizza: Pizza):
        self._pizza = pizza
        
    @abstractmethod
    def cost(self):
        pass
    
    @abstractmethod
    def get_description(self):
        pass
    
class CheeseTopping(PizzaDeccorator):

    def cost(self):
        return self._pizza.cost() + 1

    def get_description(self):
        return self._pizza.get_description() + " add Cheese Topping"
        
        
class OlivesTopping(PizzaDeccorator):

    def cost(self):
        return self._pizza.cost() + 1

    def get_description(self):
        return self._pizza.get_description() + " add Olives Topping"
        

class MushroomsTopping(PizzaDeccorator):

    def cost(self):
        return self._pizza.cost() + 1

    def get_description(self):
        return self._pizza.get_description() + " add Mushrooms Topping"
        
        
class PepperoniTopping(PizzaDeccorator):

    def cost(self):
        return self._pizza.cost() + 1

    def get_description(self):
        return self._pizza.get_description() + " add Pepperoni Topping"
        
        
# --------- Challenge: Notification System ---------
"""
You're building a Notification System for an application. 
The system sends notifications to users, but it needs to support multiple communication channels, such as:

    - Email
    - SMS
    - Push Notifications
    
Each notification can be sent through multiple channels. 
For example, you might send a Push Notification and Email to the same user.

    1- Create a base Notification class.
    2- Create decorators for the following notification types:
        - EmailNotification
        - SMSNotification
        - PushNotification
        
    3- The decorators should add the respective functionality to the base notification.
    4- Add a send() method that will send the notification and print the method of sending.
    5- Finally, create a NotificationSystem that sends notifications via different combinations of these channels.
    
Instructions:
    1- Define a Notification base class.
    2- Create decorators for each notification channel (Email, SMS, Push).
    3- Combine the decorators to send a notification through multiple channels.
    4- Print which channels the notification was sent through.
"""

# Answer
class Notification(ABC):
    @abstractmethod
    def send(self):
        pass
    
class BaseNotification(Notification):
    def send(self):
        return "This is Notification"


class NotificationDecorator(Notification):
    def __init__(self, notification: Notification):
        self._notification = notification
       
    @abstractmethod    
    def send(self):
        pass
    
class EmailNotification(NotificationDecorator):
    def send(self):
        return self._notification.send() + " by Email" 

class SMSNotification(NotificationDecorator):
    def send(self):
        return self._notification.send() + " by SMS" 


class PushNotification(NotificationDecorator):
    def send(self):
        return self._notification.send() + " by PUSH" 


base_notif = BaseNotification()

email_notif = EmailNotification(base_notif)
print(email_notif.send())
sms_notif = SMSNotification(email_notif)
print(sms_notif.send())
push_notif = PushNotification(sms_notif)
print(push_notif.send())
