class Rectangle:
            
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width


    @width.setter
    def width(self, new_width):
        self.__width = new_width


    @property
    def height(self):
        return self.__height

        
    @height.setter
    def height(self, new_height):
        self.__height = new_height


    def get_area(self):
        return self.__width * self.__height