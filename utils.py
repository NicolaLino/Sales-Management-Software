from models import Product, Supermarket
from typing import Dict, List

warehouse: Dict[int, Product] = {}
supermarket: Dict[int, Supermarket] = {}


def read_warehouse_file():
    from os import getcwd

    p = getcwd()
    try:
        with open(f"{p}/warehouse_items.txt", "r") as f:
            for line in f:
                try:
                    code, name, ex_date, w_cost, s_cost, quantity = line.strip().split(';')
                except ValueError:
                    return
                warehouse[int(code)] = Product(int(code), name, ex_date,
                                               float(w_cost), float(s_cost), int(quantity))
    except FileNotFoundError:
        print("There is No Product in the Warehouse")
        return


def write_warehouse_file():

    with open("warehouse_items.txt", "w") as f:
        for key in warehouse.keys():
            f.write(f"{warehouse[int(key)]}\n")


def is_integer(s):

    try:
        return int(s)
    except ValueError:
        return None


def is_float(s):

    try:
        return float(s)
    except ValueError:
        return None


''' 
Main Menu Commands Functions

'''

''' 1. Add product items to the warehouse  '''


def add_new_product():

    code = is_integer(input("Enter Product ID: "))
    if code is None or not Product.is_valid_code(code):
        print("Invalid input")
        return
    if code in warehouse:
        raise KeyError("Code is not unique")

    name = input("Enter Product name: ")
    expiry_date = input("Enter Product expiry date: ")
    w_cost = is_float(input("Enter whole sale cost: "))
    s_cost = is_float(input("Enter sale cost: "))
    quantity = is_integer(input("Enter Product quantity: "))

    if w_cost is None or s_cost is None or quantity is None:
        print("\nInvalid input")
        return
    else:
        warehouse[code] = Product(code=code, name=name, expiry_date=expiry_date,
                                  wholesale_cost=w_cost, sales_cost=s_cost, quantity=quantity)


''' 2. Add a new supermarket to the management system   '''


def add_new_supermarket():

    code = is_integer(input("Enter Supermarket ID: "))

    if code is None or not Product.is_valid_code(code):
        print("Invalid input")
        return
    if code in supermarket:
        raise KeyError("Code is not unique")

    name = input("Enter Supermarket name: ")
    add = input("Enter Supermarket Address: ")

    supermarket[code] = Supermarket(code=code, name=name, address=add)
    print(f"Supermarket Added Date: {supermarket[code].added_date}")
