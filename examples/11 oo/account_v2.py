class Account: 
    numCreated = 0
    
    def __init__(self, number, name='Anon', initial=0): 
        self.__number = number 
        self.__name = name 
        self.__balance = initial 
        Account.numCreated += 1
        
    def deposit(self, amt): 
        self.__balance = self.__balance + amt
        
    def withdraw(self,amt): 
        self.__balance = self.__balance - amt 

    def     
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name 
     
    @property
    def balance(self): 
        return self.__balance 
