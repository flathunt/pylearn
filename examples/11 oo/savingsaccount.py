from account import Account

class SavingsAccount(Account): 
    numCreated = 0
    
    def __init__(self, initial, int_rate): 
        super().__init__(initial) 
        self.__int_rate = int_rate

    def add_int(self):
        pass
        
