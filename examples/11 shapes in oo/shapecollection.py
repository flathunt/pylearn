# collection for shapes


class ShapeCollection:

    def __init__(self):
        self._index = None
        self._shapes = []

    def add(self, shape):
        self._shapes.append(shape)

    def __iter__(self):
        self._index = -1
        return self

    def __next__(self):        
        if self._index == len(self._shapes) - 1:
            raise StopIteration
            
        self._index += 1
        return self._shapes[self._index]

    def __len__(self):
        return len(self._shapes)

    @property        
    def area(self):      
        return sum(s.area for s in self._shapes)
