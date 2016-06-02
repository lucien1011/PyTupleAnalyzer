
import ROOT

##__________________________________________________________________||

class TreeHandler(object):
    """
    class that deal with the IO of ROOT trees
    instances of this class are used by looper to run analysis 
    """
    def __init__(self):
        self.treeList = []
        self.fileList = []

    def addTree(self,tree):
        self.treeList.append(tree)

    def readTreeFromFile(self,filePath,treePath):
        file = ROOT.TFile(filePath,"READ")
        tree = file.Get(treePath)
        self.fileList.append(file)
        self.addTree(tree)

        
