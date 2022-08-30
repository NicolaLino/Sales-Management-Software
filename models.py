
from typing import List, Dict



class Product():
    ''' Class for products in the warehouse '''
    def __init__(self, code: int, name: str, expiry_date: str, wholesale_cost: float, sales_cost: float, quantity: int) -> None:
        self.code = code
        self.name = name
        self.expiry_date = expiry_date
        self.wholesale_cost = wholesale_cost
        self.sales_cost = sales_cost
        self.quantity = quantity

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

    def __str__(self) -> str:
        return f"{self.code};{self.name};{self.expiry_date};{self.wholesale_cost};{self.sales_cost};{self.quantity}"

    def print_product(self):
        return f"Code : {self.code}, Name: {self.name}, Expiry Date: {self.expiry_date}, Wholesale Cost: {self.wholesale_cost}, Sales Cost: {self.sales_cost}, Quantity: {self.quantity}"


class Supermarket():
    ''' class for supermarket '''
    def __init__(self, code: int, name: str, address: str, added_date: str, items: Dict[int, list] = None) -> None:
        self.code = code
        self.name = name
        self.address = address
        self.added_date = added_date
        if items is None:
            self.items: Dict[int, list] = {}
        else:
            self.items = items

    def add_item(self, pid: int, q: int):
        if pid not in self.items:
            self.items[pid] = [pid, q]

    def remove_item(self, id):
        if id in self.items:
            del self.items[id]

    def __str__(self) -> str:
        return f"{self.code};{self.name};{self.address};{self.added_date}"

    def print_supermarket(self, id):
        return f"Code : {self.code}, Name: {self.name}, Address: {self.address}, items[ code: {id}, quantity: {self.items[id][1]}]"
