class Date:
 
    def __init__(self, day=0, month=0, year=0):
        self.__day   = day
        self.__month = month
        self.__year  = year

    def __str__(self):
        return "{:02d}/{:02d}/{:d}".format(
            self.__day, self.__month, self.__year)
               
    def __add__ (self, value):
        retn = Date(self.__day, self.__month, self.__year)
        retn.__day = retn.__day + value
        retn.__validate_date()
        return retn

    def __validate_date(self):
        pass

