

class ntm:
    def printer1(self):
        print("hello world #111")
        
    def printer2(self):
        print("hello world #22222")
        
        
    def printy(self):
        x = int(input("what u want fam? "))
        mydic = {1:self.printer1, 2:self.printer2}
        mydic[x]()
        
ntm().printy()
    
