from Warehouse import MainWarehouse
from typing import Callable
import time

def warehousemenu() -> int:
    '''
    Provides an interface to pick the warehouse location the user wishes to access

    Output
    ------
    Returns the int value of the user's choice
    '''
        
    #Options menu 
    print("")
    print("===== APP 2022 WAREHOUSE MANAGER =====")
    print("======================================")
    print("========== SELECT WAREHOUSE ==========")
    print("(1) - Barcelona - Poblenou")
    print("(2) - Paris - Place d'Italie")
    print("")
    
    #User inputs choice
    choice = input("Your choice (type 1 or 2):  ")
    
    #Return the choice
    return int(choice )
    
    
def warehouse_loader(choice: int = warehousemenu()) -> Callable:
    '''
    Loads the selected warehouse location

    Output
    ------
    Returns the menu display function for the selected warehouse from the MainWarehouse class
    -> see Warehouse.py
    '''
    
    
    
    #Dict storing the strings for chosen warehouse
    loc_dict = {1: "Barcelona",
                2:"Paris"}
    
    #Display choice and call the menu display of selected warehouse
    print(f"Loading {loc_dict[choice]} Warehouse...")
    time.sleep(1)
    print("")
    print("===== APP 2022 WAREHOUSE MANAGER =====")
    print(f"========= {loc_dict[choice].upper()} LOCATION =========")
    loc_dict[choice] = MainWarehouse()
    return loc_dict[choice].display_menu()
    
    

warehouse_loader()   