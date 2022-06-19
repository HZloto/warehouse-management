#IMPORTS
import time
import datetime
from typing import Callable
from Stock import Redwood, Maple, Oak

def test_warehouse():
    '''
    This function tests the functionalities of the warehouse management app 
    by brute forcing inputs and asserting that returns are integers
    '''
    mywarehouse = MainWarehouse()

    mywarehouse.add_stock()
    assert type(mywarehouse.add_stock()) is int
    
    mywarehouse.remove_stock()
    assert type(mywarehouse.remove_stock()) is int
    
    mywarehouse.get_stock()
    assert type(mywarehouse.get_stock()) is int
    
    mywarehouse.display_inventory()
    for i in mywarehouse.display_inventory():
        if i == int:
            pass
    
    
    print("ADD_STOCK UNITTEST PASSED")
    print("REMOVE_STOCK UNITTEST PASSED")
    print("GET_STOCK UNITTEST PASSED")
    print("DISPLAY_INVENTORY UNITTEST PASSED")
    time.sleep(0.2)
    print("#")
    time.sleep(0.2)
    print("##")
    time.sleep(0.2)
    print("###")
    print("ALL TESTS PASSED - EXITING TEST FILE")
    exit()
        


#####################################
#The Following is the MainWarehouse class with user inputs swiched for pre-picked value
#THIS IS NOT PRODUCTION CODE - DISREGARD
#####################################


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
        
        stock_type = 1    
        
        
        #Check input validity
        self.input_check(stock_type)
        
        #User inputs the quantity he/she wishes to add
        stock_quantity = 100
        
        #Check input validity
        if stock_quantity > 0 :
            pass   
        else:
            print("ERROR: Please enter a valid quantity.")
           
            self.add_stock()
        
        #Call add_stock
        self.stocktypedict_[int(stock_type)].add_stock(stock_quantity)
        
        #Display confirmation of execution then return to menu
        
        
        return stock_quantity
            
        
        
        
    def remove_stock(self) -> Callable:
        '''
        Provides an interface to pick stock type to remove, and what quanitity
            
        Output
        ------
        Saves the changes in the local class memory
        -> Returns the main menu function after displaying successful changes
        '''
        
        
        stock_type = 1
       
        
        #Check input validity
        self.input_check(stock_type)
        
        #Get remaining stock
        remaining_stock = self.stocktypedict_[int(stock_type)].quantity
        
        stock_quantity = 1
        
        #Check input validity
        if stock_quantity > 0 :
            pass   
        else:
            print("ERROR: Please enter a valid quantity.")
            
            self.remove_stock()
        
        
        if self.stocktypedict_[int(stock_type)].quantity - stock_quantity >= 0:
        #Do the operation
            self.stocktypedict_[stock_type].remove_stock(stock_quantity)
        #Display confirmation of execution and remaining stock then return to menu
            
            return stock_quantity
        else:
        #Display error message and call the remove function again
            print("")
            print("ERROR: Stock cannot be negative. Please try again.")
           
            return stock_quantity
        
        
        
    def get_stock(self) -> Callable:
        '''
        Lets the user get a report on an individual stock
                  
        Output
        ------
        Prints a statement with the quantity of a stock available
    
        '''  
        
        #Options menu
       
        stock_type = 1
        
        #Check input validity
        self.input_check(stock_type)
    
        
        #Get remaining stock
        remaining_stock = self.stocktypedict_[int(stock_type)].quantity
        
        #Use the remaining_stock variable and the user input to write the sentence
        print(f"{remaining_stock} pallet(s) of {self.stocktypedict_[int(stock_type)].name} worth {self.stocktypedict_[int(stock_type)].unit_price*remaining_stock}€ are left in the stock. ")
        
        print("======================================")
        
        #User need to press a button to come back to the menu
        return(remaining_stock)
        
        
        
        
    def display_inventory(self) -> Callable:
        '''
        gives the user a full report of the inventory with the option to save the report as a .txt file
            
        Output
        ------
        Prints inventory report
        -> optionally saves a txt file.
        '''
         
        #show options
        
        save_choice = 'n'
        
       
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
            return(indiv_list)
        
        #Ask the user to retry in case the input is not recognised
        else: 
            print("Invalid character. Please enter (y) or (n) to continue.")
            print('')
            print('')
            return(self.display_inventory())
         
    
    
    
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
            
            self.display_menu()
        
    
    
    
test_warehouse()