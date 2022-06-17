class GenericStock:
    '''
    This class defines a generic stock type and methods to add and remove stock
    
    '''
    
    def __init__(self, unit_price: int , quantity: int, name: str) -> None:
        self.unit_price = unit_price
        self.quantity = quantity
        self.name = name 
        
    def add_stock(stock_type: str, quantity: int) -> None:
        stock_type.quantity += quantity
         
        
    def remove_stock(stock_type: str, quantity: int) -> None:
        stock_type.quantity -= quantity
        
#Using class inheritance we define three stock types
## We add an additionnal attribute that is unique to each wood type

class Redwood(GenericStock):
    def __init__(self, unit_price: int, quantity: int) -> None:
        super().__init__(unit_price, quantity, name = "Redwood")
        self.density_ = 5
        
class Maple(GenericStock):
    def __init__(self, unit_price: int, quantity: int) -> None:
        super().__init__(unit_price, quantity, name = "Maple")
        self.humidity_ = 10  

class Oak(GenericStock):
    def __init__(self, unit_price: int, quantity: int) -> None:
        super().__init__(unit_price, quantity, name = "Oak")
        self.varnish_ = "Bright"
