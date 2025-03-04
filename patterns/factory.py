from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def get_specs(self):
        pass

class Smartphone(Device):
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery

    def get_specs(self):
        return f"Смартфон {self.brand} {self.model}, батарея: {self.battery} мАг"

class Laptop(Device):
    def __init__(self, brand, model, ram):
        self.brand = brand
        self.model = model
        self.ram = ram

    def get_specs(self):
        return f"Ноутбук {self.brand} {self.model}, ОЗП: {self.ram} ГБ"


class DeviceFactory(ABC):
    @abstractmethod
    def create_device(self) -> Device:
        pass


class SmartphoneFactory(DeviceFactory):
    def create_device(self):
        return Smartphone("Apple", "iPhone 15", 4000)

class LaptopFactory(DeviceFactory):
    def create_device(self):
        return Laptop("Dell", "XPS 15", 16)

smartphone_factory = SmartphoneFactory()
laptop_factory = LaptopFactory()

smartphone = smartphone_factory.create_device()
laptop = laptop_factory.create_device()

print(smartphone.get_specs())
print(laptop.get_specs())
