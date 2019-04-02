class Rectangle:        
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height
        
    def get_area(self):
        return self.width * self.height

