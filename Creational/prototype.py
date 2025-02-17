import copy


class Prototypt:
    def __init__(self):
        self._objects = {}

    def register(self, name, obj):
        self._objects[name] = obj

    def unregister(self, name):
        del self._objects[name]

    def clone(self, name, **kwargs):
        cloned_obj = copy.deepcopy(self._objects.get(name))
        cloned_obj.__dict__.update(kwargs)
        return cloned_obj


def client_prototype(name, obj, **kwargs):
    prototype = Prototypt()
    prototype.register(name, obj)
    return prototype.clone(name, **kwargs)


# ------Example-------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person('Farzin', 34)

clone_p = client_prototype('p1', p)


print(clone_p.__dict__)
