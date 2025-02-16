from abc import ABC, abstractmethod


class Car(ABC):  # Abstract Factory
    @abstractmethod
    def call_suv(self):
        pass

    @abstractmethod
    def call_coupe(self):
        pass


class Benz(Car):  # Concrete Factory1
    def call_suv(self):
        return Gla()

    def call_coupe(self):
        return Cls()


class Bmw(Car):  # Concrete Factory2
    def call_suv(self):
        return X1()

    def call_coupe(self):
        return M2()


class Suv(ABC):  # Abstract Product A
    @abstractmethod
    def create_suv(self):
        pass


class Coupe(ABC):  # Abstract Product B
    @abstractmethod
    def create_coupe(self):
        pass


class Gla(Suv):  # Concrete Product A1
    def create_suv(self):
        print("This is your suv Benz gla.")


class Cls(Coupe):  # Product B1
    def create_coupe(self):
        print("This is your coupe Benz cls.")


class M2(Coupe):  # Concrete Product B2
    def create_coupe(self):
        print("This is your coupe Bmw m2.")


class X1(Suv):  # Concrete Product A2
    def create_suv(self):
        print("This is your suv Bmw x1.")


def client_suv(brand):  # Client
    brands = {
        'benz': Benz,
        'bmw': Bmw
    }
    suv = brands[brand]().call_suv()
    suv.create_suv()


def client_coupe(brand):  # Client
    brands = {
        'benz': Benz,
        'bmw': Bmw
    }
    coupe = brands[brand]().call_coupe()
    coupe.create_coupe()


client_suv('benz')
