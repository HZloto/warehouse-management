#IMPORTS
import pandas as pd
import time


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
        pass
      
    def add_stock(self, stock_df = stock_df):
        '''
        Provides an interface to pick stock type to add, and what quanitity
                
        Parameters
        ----------
            - stock_df: pandas DataFrame
                table of all the stocks
            
        Output
        ------
        Saves the changes in the local csv file
        -> Returns the main menu function after displaying successful changes
        '''
        #Options menu
        print("============== ADD STOCK =============")
        print("Pick stock type:")
        print("(1) - Redwood")
        print("(2) - Maple")
        print("(3) - Oak")
        print("======================================")
        print("")
        stock_type = int(input("Stock type:  "))
        
        #Check input validity
        if stock_type == 1 or stock_type == 2 or stock_type == 3:
            pass
        else:
            print("ERROR: Please enter a valid stock type (1, 2 or 3).")
            time.sleep(2)
            main_warehouse().add_stock()
            
        print("")
        print("======================================")
        print("")
        stock_quantity = int(input("Quantity to add:  "))
        
        #Check input validity
        if stock_quantity > 0 :
            pass   
        else:
            print("ERROR: Please enter a valid quantity.")
            time.sleep(2)
            main_warehouse().add_stock()
            
        print("")
        print("======================================")

        #Dict storing the references
        stocktypedict = {1 :'Redwood', 
                     2: 'Maple', 
                     3: 'Oak' }
        
        #Use .loc to find the corresponding cell, then add required quantity
        stock_df.loc[stock_df['Stock_type'] == stocktypedict[stock_type], "Quantity"] += stock_quantity
        
        #Save the updated df to csv
        stock_df.to_csv("stock.csv", index = False)
        
        #Display confirmation of execution then return to menu
        print("")
        print(f'Successfully added {stock_quantity} pallets of {stocktypedict[stock_type]} to the stock.')
        time.sleep(2)
        print("")
        print("======================================")
        print("Returning to menu...")
        time.sleep(1)
        
        return main_warehouse().display_menu()
            
        
    def remove_stock(self, stock_df = stock_df):
        '''
        Provides an interface to pick stock type to remove, and what quanitity
                
        Parameters
        ----------
            - stock_df: pandas DataFrame
                table of all the stocks
            
        Output
        ------
        Saves the changes in the local csv file
        -> Returns the main menu function after displaying successful changes
        '''
        #Options menu
        print("============ REMOVE STOCK ============")
        print("Pick stock type:")
        print("(1) - Redwood")
        print("(2) - Maple")
        print("(3) - Oak")
        print("======================================")
        print("")
        stock_type = int(input("Stock type:  "))
        
        #Check input validity
        if stock_type == 1 or stock_type == 2 or stock_type == 3:
            pass
        else:
            print("ERROR: Please enter a valid stock type (1, 2 or 3).")
            time.sleep(2)
            main_warehouse().remove_stock()
        
        print("")
        print("======================================")
        print("")
        stock_quantity = int(input("Quantity to remove:  "))
        
        #Check input validity
        if stock_quantity > 0 :
            pass   
        else:
            print("ERROR: Please enter a valid quantity.")
            time.sleep(2)
            main_warehouse().remove_stock()
        
        print("")
        print("======================================")

        #Dict storing the references
        stocktypedict = {1 :'Redwood', 
                     2: 'Maple', 
                     3: 'Oak' }
        
        #Use .loc to find the corresponding cell, then remove required quantity
        stock_df.loc[stock_df['Stock_type'] == stocktypedict[stock_type], "Quantity"] -= stock_quantity
        
        #Save the updated df to csv
        stock_df.to_csv("stock.csv", index = False)
        
        #Get remaining stock
        remaining_stock = int(stock_df.loc[stock_df['Stock_type'] == stocktypedict[stock_type], "Quantity"])
        
        if remaining_stock >= 0:
        #Display confirmation of execution and remaining stock then return to menu
            print("")
            print(f'Successfully removed {stock_quantity} pallets of {stocktypedict[stock_type]} to the stock.')
            print(f'{remaining_stock} pallet(s) of {stocktypedict[stock_type]} are left in the stock.')
            time.sleep(2)
            print("")
            print("======================================")
            print("Returning to menu...")
            time.sleep(1)
            
            return main_warehouse().display_menu()
        else:
        #Display error message and call the remove function again
            print("")
            print("ERROR: Stock cannot be negative. Please try again.")
            time.sleep(2)
            return main_warehouse().remove_stock()
    
    def exit_program(self):
        '''
        Calls python's exit function to leave the script.         
        '''
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
        
        #Print menu 
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
       
#Entry point      
if __name__ == "__main__":
    main_warehouse().display_menu()
            
        