from lobe import Lobe
from cortex import TextualCortex
from stm import STM
from ltm import LTM

class Qaint(lobe):
    def __init__(self, cortex, stm, ltm):
        self.cortex = cortex
        self.cortex.setParent(self)
        self.stm = stm
        self.stm.setParent(self)
        self.ltm = ltm
        self.ltm.setParent(self)
    def iterate(self):
        self.cortex.fire()
