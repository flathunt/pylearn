class Account: 
    numCreated = 0
    
    def __init__(self, initial): 
        self.__balance = initial 
        Account.numCreated += 1
        
    def deposit(self, amt): 
        self.__balance = self.__balance + amt
        
    def withdraw(self,amt): 
        self.__balance = self.__balance - amt 
        
    def getbalance(self): 
        return self.__balance 
