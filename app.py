from secrets import choice
from utils import *

def main():
    while(True):
    
        print("""\n 
_________________________________

\t\t Menu
_________________________________\n
1- Add new product item to the ware house.
2- Add new supermarket to the management system.
3- List of items in the warehouse based on expiry date.
4- Clear an item from the warehouse.
5- Distribute products from the warehouse to a supermarket.
6- Generate a report about the sales status of the warehouse.
7- Exit\n
Enter Command Number: 
            """)
        choice = is_integer(input())

if __name__ == '__main__':
    main()