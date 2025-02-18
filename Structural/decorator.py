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
        
        

base_pizza = BasePizza()
print(base_pizza.cost())
print(base_pizza.get_description())
add_pepperoni = PepperoniTopping(base_pizza)
print(add_pepperoni.cost())
print(add_pepperoni.get_description())
add_olives = OlivesTopping(add_pepperoni)
print(add_olives.cost())
print(add_olives.get_description())