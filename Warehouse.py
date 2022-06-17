#IMPORTS
import time
import datetime
from typing import Callable
from Stock import Redwood, Maple, Oak


class MainWarehouse:
    '''
    This class provides all the functionalities required to use the app.
    
    '''    
    
    def __init__(self) -> None:
        #We create objects for our stock and define a unit price
        redwood = Redwood(unit_price = 80, quantity = 0)
        maple = Maple(unit_price = 100, quantity = 0)
        oak = Oak(unit_price = 70, quantity = 0)
    
        #Dict storing the references of stock
        self.stocktypedict_ = {1 : redwood, 
                            2 : maple, 
                            3 : oak } 
    
    
        
      
    def add_stock(self) -> Callable:
        '''
        Provides an interface to pick stock type to add, and what quanitity.
    
        Output
        ------
        Saves the changes in the local class memory
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
        stock_type = input("Stock type:  ")    
        print("")
        print("======================================")
        print("")
        
        #Check input validity
        self.input_check(stock_type)
        
        #User inputs the quantity he/she wishes to add
        stock_quantity = int(input("Quantity to add:  "))
        
        #Check input validity
        if stock_quantity > 0 :
            pass   
        else:
            print("ERROR: Please enter a valid quantity.")
            time.sleep(2)
            self.add_stock()
            
        print("")
        print("======================================")
        
        #Call add_stock
        self.stocktypedict_[int(stock_type)].add_stock(stock_quantity)
        
        #Display confirmation of execution then return to menu
        print("")
        print(f'Successfully added {stock_quantity} pallets of {self.stocktypedict_[int(stock_type)].name} to the stock.')
        time.sleep(2)
        print("")
        print("======================================")
        print("Returning to menu...")
        time.sleep(1)
        
        return self.display_menu()
            
        
        
        
    def remove_stock(self) -> Callable:
        '''
        Provides an interface to pick stock type to remove, and what quanitity
            
        Output
        ------
        Saves the changes in the local class memory
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
        print("")
        print("======================================")
        print("")
        
        #Check input validity
        self.input_check(stock_type)
        
        #Get remaining stock
        remaining_stock = self.stocktypedict_[int(stock_type)].quantity
        
        print(f"There are currently {remaining_stock} pallet(s) left of {self.stocktypedict_[int(stock_type)].name}. ")
        print('')
        stock_quantity = int(input("Quantity to remove:  "))
        
        #Check input validity
        if stock_quantity > 0 :
            pass   
        else:
            print("ERROR: Please enter a valid quantity.")
            time.sleep(2)
            self.remove_stock()
        
        print("")
        print("======================================")
        
        if self.stocktypedict_[int(stock_type)].quantity - stock_quantity >= 0:
        #Do the operation
            self.stocktypedict_[stock_type].remove_stock(stock_quantity)
        #Display confirmation of execution and remaining stock then return to menu
            print("")
            print(f'Successfully removed {stock_quantity} pallets of {self.stocktypedict_[int(stock_type)].name} to the stock.')
            print(f'{self.stocktypedict_[stock_type].quantity} pallet(s) of {self.stocktypedict_[int(stock_type)].name} are left in the stock.')
            time.sleep(2)
            print("")
            print("======================================")
            print("Returning to menu...")
            time.sleep(1)
            
            return self.display_menu()
        else:
        #Display error message and call the remove function again
            print("")
            print("ERROR: Stock cannot be negative. Please try again.")
            time.sleep(2)
            return self.remove_stock()
        
        
        
    def get_stock(self) -> Callable:
        '''
        Lets the user get a report on an individual stock
                  
        Output
        ------
        Prints a statement with the quantity of a stock available
    
        '''  
        
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
        self.input_check(stock_type)
        
        #Visuals and print of today's date    
        print("")
        print("======================================")
        print(f"{str(self.stocktypedict_[int(stock_type)].name).upper()} REPORT:")
        today = datetime.date.today()
        print(f"As of {today},")
        
        #Get remaining stock
        remaining_stock = self.stocktypedict_[int(stock_type)].quantity
        
        #Use the remaining_stock variable and the user input to write the sentence
        print(f"{remaining_stock} pallet(s) of {self.stocktypedict_[int(stock_type)].name} worth {self.stocktypedict_[int(stock_type)].unit_price*remaining_stock}€ are left in the stock. ")
        
        print("======================================")
        
        #User need to press a button to come back to the menu
        return(input("Hit 'Enter' to return to main menu."), self.display_menu())
        
        
        
        
    def display_inventory(self) -> Callable:
        '''
        gives the user a full report of the inventory with the option to save the report as a .txt file
            
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
        
        for i in self.stocktypedict_:
            remaining_stock = self.stocktypedict_[i].quantity
            indiv_stock = f"{remaining_stock} pallets of { self.stocktypedict_[i].name} worth {remaining_stock*self.stocktypedict_[i].unit_price}€"
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
            return(input("Hit 'Enter' to return to main menu."), self.display_menu())
                
        #Case if the user doesn't want to save
        elif save_choice == "n":
            return(input("Hit 'Enter' to return to main menu."), self.display_menu())
        
        #Ask the user to retry in case the input is not recognised
        else: 
            print("Invalid character. Please enter (y) or (n) to continue.")
            print('')
            print('')
            return(self.display_inventory())
         
    
    def exit_program(self) -> None:
        '''
        Calls python's exit function to leave the script.         
        '''
        print("exiting program...")
        print("exited.")
        exit()
        
    
    def input_check(self, input: int) -> None:
        '''
        ensures that user input is an integer
        
        '''
        input = int(input)
        
        if input in [1,2,3,4,5]:
            return input
            
        else:
            print (("ERROR: Please enter a valid input."))
            print("")
            time.sleep(1)
            self.display_menu()
        
        

    def display_menu(self) -> Callable:
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
        request = input("Input request:  ") 
        print("")
        print("======================================")
        print("")
        
        
        #Check input validity
        self.input_check(request)
        
        #Dictionnary with references to all menu items
        menu = {1: self.add_stock,
                2: self.remove_stock, 
                3: self.get_stock,
                4: self.display_inventory, 
                5: self.exit_program} 
        
        #Using request #, returns a call to the function
        return menu[int(request)]() 
    