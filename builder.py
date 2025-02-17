from abc import ABC, abstractmethod


class Car:

    def __init__(self):
        self._wheel = None
        self._engine = None
        self._body = None

    def set_wheel(self, wheel):
        self._wheel = wheel

    def set_body(self, body):
        self._body = body

    def set_engine(self, engine):
        self._engine = engine

    def detail(self):
        print(f"Body: {self._body.shape}")
        print(f"Engone: {self._engine.hp}")
        print(f"Wheel: {self._wheel.size}")


class AbstractBuilder(ABC):  # Abstract Builder

    @abstractmethod
    def get_engine(self): pass

    @abstractmethod
    def get_body(self): pass

    @abstractmethod
    def get_wheel(self): pass


class Benz(AbstractBuilder):  # Concrete Builder 1
    def get_body(self):
        body = Body()
        body.shape = 'suv'
        return body

    def get_engine(self):
        engine = Engine()
        engine.hp = 500
        return engine

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel


class Bmw(AbstractBuilder):  # Concrete Builder 2
    def get_body(self):
        body = Body()
        body.shape = 'sedan'
        return body

    def get_engine(self):
        engine = Engine()
        engine.hp = 380
        return engine

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 20
        return wheel


class Director:
    _builder = None

    def set_builder(self, builder):
        self._builder = builder

    def construct(self):
        car = Car()
        body = self._builder.get_body()
        car.set_body(body)

        wheel = self._builder.get_wheel()
        car.set_wheel(wheel)

        engine = self._builder.get_engine()
        car.set_engine(engine)

        return car


# ----Optional----
class Body:
    shape = None


class Wheel:
    size = None


class Engine:
    hp = None


# ---Test Code---

def client_builder(builder):
    builders = {
        'bmw': Bmw,
        'benz': Benz
    }

    car = builders[builder]()
    director = Director()
    director.set_builder(car)
    result = director.construct()
    return result.detail()


client_builder('benz')
