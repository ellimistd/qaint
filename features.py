class Feature:
    pass
    
class Qualia(Feature):
    def __init__(self, data):
        self.data = data
        
    #def __equals__(self, other):
        #return self.data == other.data
    
class Relation(Feature):
    def __init__(self, data, a, b):
        self.data = data
        self.a = a
        self.b = b
        
    def __equals__(self, other):
        return self.data == other.data and self.a == other.a and self.b == other.b
