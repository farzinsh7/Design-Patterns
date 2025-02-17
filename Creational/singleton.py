# First Method
class A:
    _instance = None

    def __init__(self):
        raise RuntimeError("Call get_instance() instead.")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance


a1 = A.get_instance()
a2 = A.get_instance()

print(id(a1))
print(id(a2))


# Second Method
class Singleton(type):
    _instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__(*args, **kwargs)
        return self._instance


class B(metaclass=Singleton):
    pass


b1 = B()
b2 = B()

print(id(b1))
print(id(b2))
