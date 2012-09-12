from lobe import Lobe
from features import Qualia

class TextualCortex(Lobe):
    def __init__(self, world):
        self.data = None
        self.world = world
        
    def fire(self):
        self.text = world.getView()
        self.parent.stm.fire()
    
    #~ def findQualia(self,letter):
        #~ if self.parent.ltm.hasQualiaFor(letter):
            #~ return self.parent.ltm.getQualiaFor(letter)
        #~ else:
            #~ return Qualia(letter)
            
    def getText(self):
        return self.text
        
        
class StreetWorld:
    def __init__(self, fileloc):
        self.text = open(fileloc,'r')
    def getView(self,**data):
        return self.text.readline()
