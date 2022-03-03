from StructureTB import StructureTB
from Two_Bag import Two_Bag
from TNode import TNode

class Tree_Descomposition:

    def __init__(self,sampleTree,myTwoBag):
        self.sampleTree = sampleTree
        self.structure = myTwoBag
        self.twoBag = Two_Bag(sampleTree,myTwoBag)

    def createBagTree(self):
        contBag = 0
        self.structure.fillQueues(self.sampleTree)
        #self.structure.printQueue(self.structure.Q1)
        cont = 0
        while(len(self.structure.Q1) > 0 and cont < 6):
            xVertex1:TNode = self.structure.dequeue(self.structure.Q1)
            #print(xVertex1)
            contBag = contBag + 1
            self.twoBag.createTwoBag(xVertex1,contBag)
            cont = cont + 1