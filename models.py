''' Python Classes '''

from typing import List, Tuple
from datetime import date


class Product():

    def __init__(self, code: int, name: str, expiry_date: str, wholesale_cost: float, sales_cost: float, quantity: int) -> None:
        self.code = code
        self.name = name
        self.expiry_date = expiry_date
        self.wholesale_cost = wholesale_cost
        self.sales_cost = sales_cost
        self.quantity = quantity

    @property
    def ID(self):
        return self.ID
    
    # @ID.setter
    # def ID(self, value):
    #     self.ID = value

    # @name.setter
    # def name(self, value):
    #     self.name = value

    # @expiry_date.setter
    # def expiry_date(self, value):
    #     self.expiry_date = value

    # @wholesale_cost.setter
    # def wholesale_cost(self, value):
    #     self.wholesale_cost = value

    # @sales_cost.setter
    # def sales_cost(self, value):
    #     self.sales_cost = value

    # @quantity.setter
    # def quantity(self, value):
    #     self.quantity = value

    def __str__(self) -> str:
        return f"{self.ID};{self.name};{self.expiry_date};{self.wholesale_cost};{self.sales_cost};{self.quantity}"

    @staticmethod
    def is_valid_code(code_str):
        code = None

        try:
            code = int(code_str)
        except ValueError:
            return None
        if len(code) == 4:
            return code
        return None


class Supermarket():
    def __init__(self, code, name, address, items=None) -> None:
        self.code = code
        self.name = name
        self.address = address
        self.added_date = date.today()
        if items is None:
            self.items = []
        else:
            self.items = items

    # @code.setter
    # def code(self, value):
    #     self.code = value

    # @name.setter
    # def name(self, value):
    #     self.name = value

    # @address.setter
    # def address(self, value):
    #     self.address = value
    
    def add_item(self, itm):
        if itm not in self.items:
            self.items.append(itm)

    def remove_item(self, itm):
        if itm in self.items:
            self.items.remove(itm)



