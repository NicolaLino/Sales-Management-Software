''' Python Classes '''

from typing import List, Tuple
from datetime import datetime


class Product():

    def __init__(self, code: int, name: str, expiry_date: str, wholesale_cost: float, sales_cost: float, quantity: int) -> None:
        self.code = code
        self.name = name
        self.expiry_date = expiry_date
        self.wholesale_cost = wholesale_cost
        self.sales_cost = sales_cost
        self.quantity = quantity


    def __str__(self) -> str:
        # return f"Code : {self.code}, Name: {self.name}, Expiry Date: {self.expiry_date}, Wholesale Cost: {self.wholesale_cost}, Sales Cost: {self.sales_cost}, Quantity: {self.quantity}"
        return f"{self.code};{self.name};{self.expiry_date};{self.wholesale_cost};{self.sales_cost};{self.quantity}"

    @staticmethod
    def is_valid_code(code_str):
        code = None

        try:
            code = int(code_str)
        except ValueError:
            return None
        if len(str(code)) == 4:
            return code
        return None


class Supermarket():
    def __init__(self, code: int, name: str, address: str, items: Product = None) -> None:
        self.code = code
        self.name = name
        self.address = address
        self.added_date = datetime.now().strftime("%d/%m/%Y")
        if items is None:
            self.items = []
        else:
            self.items = items

    def add_item(self, itm):
        if itm not in self.items:
            self.items.append(itm)

    def remove_item(self, itm):
        if itm in self.items:
            self.items.remove(itm)
