#IMPORTS
import pandas as pd


class generic_stock:
    def __init__(self, unit_price, quantity):
        self.unit_price = unit_price
        self.quantity = quantity
    pass
    
class stock1(generic_stock):
    pass

class stock2(generic_stock):
    pass

class stock3(generic_stock):
    pass
    
    
class warehouse:
    def __init__(self,address,capacity,):
        self.address = address
        self.capacity = capacity
        

    
    
class main_warehouse:
    
    try:
        stock_df = pd.read_csv("stock.csv")
    except:
        data = {'Stock_type': ['Redwood', 'Maple', 'Oak'], 'Quantity': [0, 0, 0]}  
        stock_df = pd.DataFrame(data)
             
        
    def get_stock(self):
        print("ok")
      
    def add_stock(self, stock_df = stock_df):
        
        print("============== ADD STOCK =============")
        print("Pick stock type:")
        print("(1) - Redwood")
        print("(2) - Maple")
        print("(3) - Oak")
        print("======================================")
        print("")
        stock_type = int(input("Stock type:  "))
        print("")
        print("======================================")
        print("")
        stock_quantity = int(input("Quantity:  "))
        print("")
        print("======================================")

        stocktypedict = {1 :'Redwood', 
                     2: 'Maple', 
                     3: 'Oak' }
        
        stock_df.loc[stock_df['Stock_type'] == stocktypedict[stock_type], "Quantity"] += stock_quantity
        
        stock_df.to_csv("stock.csv", index = False)
        
        
        
        
        
              
        
    def remove_stock(self):
        pass 
    
    def exit_program(self):
        print("exiting program...")
        print("")
        exit()
        

    def display_menu(self):
        '''
        Prints the different choices presented to the user and execute the function of the chosen path.
                
        Output
        ------
        calls the function associated to the user request 
        -> Breaks if request is 5 
        '''
        
        #Printed menu 
        print("")
        print("===== APP 2022 WAREHOUSE MANAGER =====")
        print("======================================")
        print("")
        print("================ MENU ================")
        print("(1) - Inventory Report")
        print("(2) - Add Stock")
        print("(3) - Remove Stock")
        print("(4) - Inventory Report")
        print("(5) - Exit")
        print("======================================")
        print("")
        request = int(input("Input request:  "))
        print("")
        print("======================================")
        print("")
        
        #Dictionnary with references to all menu items
        menu = {1: self.get_stock, 
                2: self.add_stock,
                3: self.remove_stock, 
                4: self.get_stock, 
                5: self.exit_program} 
        
        #Using request #, returns a call to the function
        return menu[request]() 
       
        
if __name__ == "__main__":
    main_warehouse().display_menu()
            
        