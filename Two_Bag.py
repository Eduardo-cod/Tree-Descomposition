from Bag_1 import Bag_1
from StructureTB import StructureTB

class Two_Bag():

    def __init__(self, sampleTree,structure):
        self.sampleTree = sampleTree
        self.structure = structure

    def createTwoBag(self,xVertex1,contBag):
        newBagNode = Bag_1(contBag,False)
        if contBag == 1:
            self.structure.headNode = newBagNode
            #print(self.structure.headNode)
        xVertex2 = self.structure.extract_Single(self.sampleTree,xVertex1)
        newBagNode.vertex2 = xVertex2
        #print(f'vecinos de {xVertex1}: ',xVertex2)
        tempDegree = xVertex2._volatileDegree
        #print(tempDegree)
        if tempDegree == 1:
            self.structure.Q1.append(xVertex2)
            #self.structure.printQueue(self.structure.Q1)
        else:
            newDegree = self.structure.decreaseDegree(self.sampleTree,xVertex2,tempDegree)
            #print("newDegree: ",newDegree)
            xVertex2.__setvDegree__(newDegree)
            self.sampleTree = self.structure.replaceSampleTree(self.sampleTree,xVertex2)
            #print(xVertex2)
            if newDegree == 1:
                self.structure.Q1.append(xVertex2)
            else:
                self.structure.Q2.append(xVertex2)
        xVertex1.__setBaged__()
        #print(xVertex1)
        self.sampleTree = self.structure.replaceSampleTree(self.sampleTree,xVertex1)
        newBagNode.vertex1 = xVertex1
        print(f'{newBagNode}, Vertex1: {newBagNode.vertex1} Vertex2: {newBagNode.vertex2}')
        pass