from lobe import Lobe
from features import Relation

class STM(Lobe):
    def __init__(self):
        self.data = [None,None,None,None,None]
        
    def fire(self):
        self.data = [self.parent.cortex.getText()]+self.data[:4]
        for letterfeLoc in range(0,len(self.data[0])):
            self.currentLoc = (0,letterLoc)
            feature = self.parent.LTM.ask(self.currentLoc, self.data[self.currentLoc])
            
            
    def answer(self, location, expectation):
        if self.data[location[0]][location[1]] == expectation:
            return True
        else:
            return False
        
            
    def consider(self, feature):
        self.parent.LTM.ask(feature)
