#IMPORTS
import pandas as pd
import time
import datetime

#Import the csv file to store the inventory values
try:
    stock_df = pd.read_csv("stock.csv")
    
#If the file doesn't exist, we create it 
except:
    data = {'Stock_type': ['Redwood', 'Maple', 'Oak'], 'Quantity': [0, 0, 0]}  
    stock_df = pd.DataFrame(data)



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
    '''
    This class provides all the functionalities required to use the app.
    
    '''    

      
    def add_stock(self, stock_df = stock_df):
        '''
        Provides an interface to pick stock type to add, and what quanitity.
                
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
        
        #User inputs the quantity he/she wishes to add
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
        #Dict storing the references
        stocktypedict = {1 :'Redwood', 
                     2: 'Maple', 
                     3: 'Oak' }
        
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
        
        #Get remaining stock
        remaining_stock = int(stock_df.loc[stock_df['Stock_type'] == stocktypedict[stock_type], "Quantity"])
        
        print(f"There are currently {remaining_stock} pallet(s) left of {stocktypedict[stock_type]}. ")
        print('')
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
        
        #Use previously defined remaining_stock to remove required quantity to the cell of interest
        remaining_stock -= stock_quantity
        
        #Save the updated df to csv
        stock_df.to_csv("stock.csv", index = False)
        
        
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
        
        
        
    def get_stock(self, stock_df = stock_df):
        '''
        Lets the user get a report on an individual stock
                
        Parameters
        ----------
            - stock_df: pandas DataFrame
                table of all the stocks
            
        Output
        ------
        Prints a statement with the quantity of a stock available
    
        '''  
        #Dict storing the references
        stocktypedict = {1 :'Redwood', 
                     2: 'Maple', 
                     3: 'Oak' }
        
        #Options menu
        print("========== INDIVIDUAL REPORT =========")
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
        
        #Visuals and print of today's date    
        print("")
        print("======================================")
        print(f"{str(stocktypedict[stock_type]).upper()} REPORT:")
        today = datetime.date.today()
        print(f"As of {today},")
        
        #Get remaining stock
        remaining_stock = int(stock_df.loc[stock_df['Stock_type'] == stocktypedict[stock_type], "Quantity"])
        
        #Use the remaining_stock variable and the user input to write the sentence
        print(f"{remaining_stock} pallet(s) of {stocktypedict[stock_type]} are left in the stock. ")
        print("======================================")
        
        #User need to press a button to come back to the menu
        return(input("Hit 'Enter' to return to main menu."), main_warehouse().display_menu())
        
        
        
        
    def display_inventory(self, stock_df = stock_df):
        '''
        gives the user a full report of the inventory with the option to save the report as a .txt file
                
        Parameters
        ----------
            - stock_df: pandas DataFrame
                table of all the stocks
            
        Output
        ------
        Prints inventory report
        -> optionally saves a txt file.
        '''
        
         
        #show options
        print("========== INVENTORY REPORT ==========")
        
        #user inputs if a txt file should be saved
        save_choice = input("Do you wish to save a .txt file for this report? (y/n)   => ")
        
        print("")
        print("======================================")
        print(f"MAIN WAREHOUSE REPORT {datetime.date.today()}: ")
        
        #Initiate a list to store individual stock values
        indiv_list = []
        
        #Iterate thorugh stock types, print their remaining stock 
        #and saving the sentences in our list for the .txt export
        for i in stock_df['Stock_type'].tolist():
            remaining_stock = int(stock_df.loc[stock_df['Stock_type'] == str(i), "Quantity"])
            indiv_stock = f"{remaining_stock} pallets of {i}"
            indiv_list.append(indiv_stock)
            print(indiv_stock)
        print("======================================")
        print("")
            
        #Save the .txt using f.write and iterating through the indiv_list created above
        if save_choice == "y":
            with open('warehouse_report.txt', 'w') as f:
                f.write(f"MAIN WAREHOUSE REPORT {datetime.date.today()}: ")
                f.write('\n')
                for i in indiv_list:
                    f.write(i)
                    f.write('\n')
            return(input("Hit 'Enter' to return to main menu."), main_warehouse().display_menu())
                
        #Case if the user doesn't want to save
        elif save_choice == "n":
            return(input("Hit 'Enter' to return to main menu."), main_warehouse().display_menu())
        
        #Ask the user to retry in case the input is not recognised
        else: 
            print("Invalid character. Please enter (y) or (n) to continue.")
            print('')
            print('')
            return(main_warehouse().display_inventory())
         
    
    def exit_program(self):
        '''
        Calls python's exit function to leave the script.         
        '''
        print("exiting program...")
        print("exited.")
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
        print("(1) - Add Stock")
        print("(2) - Remove Stock")
        print("(3) - Individual Stock Report")
        print("(4) - Full Inventory Report")
        print("(5) - Exit")
        print("======================================")
        print("")
        request = int(input("Input request:  "))
        print("")
        print("======================================")
        print("")
        
        #Dictionnary with references to all menu items
        menu = {1: self.add_stock,
                2: self.remove_stock, 
                3: self.get_stock,
                4: self.display_inventory, 
                5: self.exit_program} 
        
        #Using request #, returns a call to the function
        return menu[request]() 
       
#Entry point      
if __name__ == "__main__":
    main_warehouse().display_menu()
            
        