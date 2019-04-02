class Car:

    # constructor

    def __init__(self, make, model, colour, reg_number):
        self.__make = make
        self.__model = model
        self.__reg_number = reg_number
        self.__colour = colour
        self.__is_running = False

    # properties...

    @property
    def make(self):
        return self.__make

    @property
    def model(self):
        return self.__model

    @property
    def reg_number(self):
        return self.__reg_number

    @reg_number.setter
    def reg_number(self, reg_number):
        self.__reg_number = reg_number

    @property
    def colour(self):
        return self.__colour

    @colour.setter
    def colour(self, colour):
        self.__colour = colour

    @property
    def status(self):
        return "running" if self.__is_running else "stopped"

    # methods...

    def start(self):
        print("Starting...")
        self.__is_running = True

    def stop(self):
        print("Stopping...")
        self.__is_running = False

    def __str__(self):
        status = f"{self.__make} {self.__model} ({self.__colour}) {self.__reg_number} is "
        status += 'running' if self.__is_running else 'stopped'
        return status

    def __repr__(self):
        status = f"Car('{self.__make}', '{self.__model}', '{self.__colour}', '{self.__reg_number}')"
        return status
