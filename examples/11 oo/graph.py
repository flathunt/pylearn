class Graph:
    
    def __init__(self, title):
        self.title = f"\n{title}:"
        self.headings = []
        self.values = []

        
    def add(self, heading, value):
        self.headings.append(heading)
        self.values.append(value)
 
        
    def plot(self):        
        print(self.title, end='\n\n')
        
        for h, v in zip(self.headings, self.values):
            print('{:10s} {}'.format(h, "=" * v))