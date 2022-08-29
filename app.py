from utils import *


def main():
    while (True):
        print_menu()
        choice = is_integer(input("Enter Command Number: "))
        print("\n")
        if choice == 1:
            try:
                add_new_product()
            except KeyError:
                print("\nCode is not unique.")
        elif choice == 2:
            try:
                add_new_supermarket()
            except KeyError:
                print("\nCode is not unique.")
        elif choice == 3:
            search_by_date()
            
        elif choice == 4:
            clear_product()
        
        elif choice == 5:
            warehouse_to_supermarkets()
        
        elif choice == 6:
            report()
        
        elif choice == 7:
            write_warehouse_file()
            write_supermarket_file()
            write_distribution_supermarkets()
            return
        else:
            print("\nEnter a Valid Input From Menu")


def print_menu():
    print("""\n 
_________________________________________________________________
|                                                               |
|                            Menu                               |
|_______________________________________________________________|
|                                                               |
| 1- Add new product item to the ware house.                    |
| 2- Add new supermarket to the management system.              |
| 3- List of items in the warehouse based on expiry date.       |
| 4- Clear an item from the warehouse.                          |
| 5- Distribute products from the warehouse to a supermarket.   |
| 6- Generate a report about the sales status of the warehouse. |
| 7- Exit                                                       |
|_______________________________________________________________|
            """)


if __name__ == '__main__':
    read_warehouse_file()
    read_supermarket_file()
    read_distribution_supermarkets()
    main()
