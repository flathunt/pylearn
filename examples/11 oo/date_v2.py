class Date:
 
    def __init__(self, day=0, month=0, year=0):
        self.__day   = day
        self.__month = month
        self.__year  = year

        
    def __str__(self):
        return "{:02d}/{:02d}/{:d}".format(
            self.__day, self.__month, self.__year)
 
 
    def __repr__(self):
        return "Date({:}, {:}, {:})".format(
            self.__day, self.__month, self.__year)

            
    def __add__ (self, value):
        if isinstance(value, int):
            retn = Date(self.__day, self.__month, self.__year)
            retn.__day = retn.__day + value
            retn.__validate_date()
            return retn
        else:
            return NotImplemented

        
    def __iadd__ (self, value):           
        self.__day += value
        self.__validate_date()
        return self  

    @property
    def mday(self):
        return self.__day
        
    @mday.setter
    def mday(self, day):
        self.__day = day    
        
    @property
    def month(self):
        return self.__month
        
    @month.setter
    def month(self, month):
        self.__month = month
       
    @property
    def year(self):
        return self.__year
        
    @year.setter
    def year(self, year):
        self.__year = year
        
    def __validate_date(self):
        # max = dict(enumerate((31,28,31,30,31,30,31,31,30,31,30,31), start=1)) 
        pass

