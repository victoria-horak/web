from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def update(self, product: str):
        pass

class Customer(Observer):
    def __init__(self, name, product_preference):
        self.name = name
        self.product_preference = product_preference

    def update(self, product: str):
        if product == self.product_preference:
            print(f"{self.name}, новий продукт у продажу: {product}")
        else:
            print(f"{self.name}, зараз в наявності продукт, який вас не цікавить.")


class TechCompany:
    def __init__(self, name):
        self.name = name
        self.subscribers: List[Observer] = []

    def subscribe(self, observer: Observer):
        self.subscribers.append(observer)

    def unsubscribe(self, observer: Observer):
        self.subscribers.remove(observer)

    def notify(self, product: str):
        for subscriber in self.subscribers:
            subscriber.update(product)

    def release_product(self, product: str):
        print(f"{self.name} випустила новий продукт: {product}")
        self.notify(product)


company = TechCompany("TechCorp")


customer1 = Customer("Вікторія", "Смартфон TechCorp X10")
customer2 = Customer("Андрій", "Ноутбук TechCorp Z50")

company.subscribe(customer1)
company.subscribe(customer2)


company.release_product("Смартфон TechCorp X10")

company.release_product("Ноутбук TechCorp Z50")

