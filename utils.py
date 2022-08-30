from models import Product, Supermarket
from typing import Dict
from os import getcwd, path
from datetime import datetime, date


warehouse: Dict[int, Product] = {}
supermarket: Dict[int, Supermarket] = {}


def read_warehouse_file():

    p = getcwd()
    try:
        with open(f"{p}/warehouse_items.txt", "r") as f:
            for line in f:
                try:
                    code, name, ex_date, w_cost, s_cost, quantity = line.strip().split(';')
                    warehouse[int(code)] = Product(int(code), name, ex_date,
                                                   float(w_cost), float(s_cost), int(quantity))
                except ValueError:
                    print(
                        "> There is invalid value in the 'warehouse_items.txt' please correct it and try again!!")
                    exit()
    except FileNotFoundError:
        print("There is No Products in the Warehouse Yet")
        return


def path_id(id: int):
    return path.join("DataBase", "DistributeItems_" + str(id) + ".txt")


def write_warehouse_file():

    with open("warehouse_items.txt", "w") as f:
        for key in warehouse.keys():
            f.write(f"{warehouse[int(key)]}\n")


def read_supermarket_file():
    p = getcwd()
    try:
        with open(f"{p}/supermarkets.txt", "r") as f:
            for line in f:
                try:
                    code, name, address, d = line.strip().split(";")
                    supermarket[int(code)] = Supermarket(
                        int(code), name, address, d)
                except ValueError:
                    print(
                        "> There is invalid value in the 'supermarkets.txt' please correct it and try again!!")
                    exit()
    except FileNotFoundError:
        print("There is No Supermarkets Yet")
        return


def write_supermarket_file():

    with open("supermarkets.txt", "w") as f:
        for key in supermarket.keys():
            f.write(f"{supermarket[int(key)]}\n")


def write_distribution_supermarkets():
    for id in [key for key in supermarket.keys()]:
        with open(path_id(id), "w") as f:
            for val in supermarket[id].items.values():
                f.write(f"{val[0]};{val[1]}\n")


def read_distribution_supermarkets():

    for id in [key for key in supermarket.keys()]:
        try:
            with open(path_id(id), "r") as f:

                # print(f"File: {id}")

                file_data = f.read()

                if len(file_data) < 2:
                    # print("File is empty")
                    return

                for line in f:
                    code, quantity = [int(x) for x in line.strip().split(";")]
                    supermarket[id].add_item(code, quantity)
        except FileNotFoundError:
            print(" ")


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
    d = datetime.now().strftime("%d/%m/%Y")
    supermarket[code] = Supermarket(
        code=code, name=name, address=add, added_date=d)
    print(f"Supermarket Added Date: {supermarket[code].added_date}")


''' 3. List of items in the warehouse based on expiry date  '''


def search_by_date():
    d, m, y = [int(x) for x in input(
        "Enter a Specific Date 'in (DD/MM/YYYY) format': ").split('/')]
    d = date(y, m, d)
    whole_sum = 0
    sale_sum = 0
    print("List of Products: \n")
    for val in warehouse.values():
        exp = val.expiry_date
        ed, em, ey = [int(x) for x in exp.split("/")]
        exp = date(int(ey), int(em), int(ed))
        if exp < d:
            print(val.print_product())
            whole_sum += val.wholesale_cost
            sale_sum += val.sales_cost

        else:
            continue

    print(f"\nThe total wholesale cost of these items: {whole_sum}")
    print(f"The total wholesale cost of these items: {sale_sum}")


''' 4. Clear an item from the warehouse  '''


def clear_product():

    code = is_integer(input("Enter Product ID: "))
    if code is None or not Product.is_valid_code(code):
        print("Invalid input")
        return
    if code not in warehouse:
        print("Product with this ID does not exist ")
        return

    print(warehouse[code].print_product())
    amount = int(input("Enter the Quantity you want to clear: "))
    if amount >= warehouse[code].quantity:
        del warehouse[code]
        print("Product was Cleared Successfully .")
    else:
        warehouse[code].quantity -= amount
        print("Quantity was updated")


'''  5. Distribute products from the warehouse to a supermarket  '''


def warehouse_to_supermarkets():
    code = is_integer(input("Enter Supermarket ID: "))

    if code is None or not Product.is_valid_code(code):
        print("Invalid input")
        return
    if code not in supermarket:
        print("Supermarket with this ID does not exist ")
        return

    pid = is_integer(input("Enter Product ID To Add it into Supermarket: "))
    if pid is None or not Product.is_valid_code(pid):
        print("Invalid input")
        return
    if pid not in warehouse:
        print("Product with this ID does not exist ")
        return
    final = 0
    print(warehouse[pid].print_product())
    amount = int(
        input("\nEnter the Quantity you want to Add to supermarket: "))

    if pid not in [key for key in supermarket[code].items.keys()]:
        if amount == warehouse[pid].quantity:
            final = warehouse[pid].quantity
            del warehouse[pid]
        elif amount > warehouse[pid].quantity:
            print("There is no Enough Quantity in the Warhorse")
            return
        else:
            warehouse[pid].quantity -= amount
            final = amount

        supermarket[code].add_item(pid, final)
    else:
        if amount == warehouse[pid].quantity:
            supermarket[code].items[pid][1] += warehouse[pid].quantity
            del warehouse[pid]
        elif amount > warehouse[pid].quantity:
            print("There is no Enough Quantity in the Warhorse")
            return
        else:
            warehouse[pid].quantity -= amount
            supermarket[code].items[pid][1] += amount

    # write_distribution_supermarkets(code)
    print(supermarket[code].print_supermarket(pid))
    print("\nProduct Was Added To Supermarket Successfully.\n")


def distribute_form_file():
    code = is_integer(input("Enter Supermarket ID: "))

    if code is None or not Product.is_valid_code(code):
        print("Invalid input")
        return
    if code not in supermarket:
        print("Supermarket with this ID does not exist ")
        return
    try:
        with open(path_id(code), "r") as f:
            for line in f:
                pid, q = [int(x) for x in line.strip().split(";")]
                if pid in warehouse:
                    if q <= warehouse[pid].quantity:
                        warehouse[pid].quantity -= q
                        supermarket[code].add_item(pid, q)
                    else:
                        supermarket[code].add_item(
                            pid, warehouse[pid].quantity)
                        print(
                            f"\nProduct [code: {pid}, name: {warehouse[pid].name}, Available: {warehouse[pid].quantity} ] Requested Amount: [{q}]")
                        warehouse[pid].quantity = 0
                else:
                    print(f"Product with ID:{pid} is not Available")

    except FileNotFoundError:
        print("File Not Found")
        return
    print("\nProduct Was Added To Supermarket Successfully.\n")


''' 6. Generate a report about the sales status of the warehouse. '''


def report():
    whole_sum = 0
    sale_sum = 0
    profit = 0
    for val in warehouse.values():
        whole_sum += val.wholesale_cost
        sale_sum += val.sales_cost

    profit = sale_sum - whole_sum
    print(f"\nNumber of items in the warehouse: {len(warehouse)}")
    print(f"\nTotal wholesale cost of all items in the warehouse: {whole_sum}")
    print(f"\nTotal sales cost of all items in the warehouse: {sale_sum}")
    print(
        f"\nExpected profit after selling all items in the warehouse: {profit}")
