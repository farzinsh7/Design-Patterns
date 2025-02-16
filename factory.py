from abc import ABC, abstractmethod

# in Factory we have 3 Components => 1.creator, 2.product, 3.client


class File(ABC):  # creator

    def __init__(self, file):
        self.file = file

    @abstractmethod
    def make(self):
        pass

    def call_edit(self):
        product = self.make()
        result = product.edit(self.file)
        return result


class JsonFile(File):  # creator
    def make(self):
        return Json()


class XmlFile(File):  # creator
    def make(self):
        return Xml()


class Json:  # product
    def edit(self, file):
        return f"Working on {file} Json..."


class Xml:  # product
    def edit(self, file):
        return f"Working on {file} Xml..."


def client(file, format):  # client
    formats = {
        'Json': JsonFile,
        'Xml': XmlFile
    }
    if format in formats:
        result = formats[format](file)
        return result.call_edit()
    else:
        return "This format is not supported bt factory"


print(client('harchi', 'Json'))
print(client('harchi1', 'Xml'))
print(client('harchi1', 'pdf'))
