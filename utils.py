from models import Product, Supermarket
from typing import Dict, List

Warehouse: Dict[int, Product] = {}



def read_file():
    from os import getcwd
    
    p = getcwd()
    with open(f"{p}/warehouse_items.txt", "r") as f:
        for lines in f:
            print(lines)
            
            

read_file()


def is_integer(s):
    
    try:
        return int(s)
    except ValueError:
        return None