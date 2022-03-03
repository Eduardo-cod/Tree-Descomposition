import networkx as nx
from StructureTB import StructureTB
from Tree_Descomposition import Tree_Descomposition
import matplotlib.pyplot as plt

if __name__ == '__main__':

    inputGraph = nx.random_tree(5)
    #nx.draw(inputGraph, with_labels=True)
    myTwoBag = StructureTB()
    myTwoBag.sampleTree = myTwoBag._tree_2_KGraph(inputGraph)
    TD = Tree_Descomposition(myTwoBag.sampleTree,myTwoBag)
    TD.createBagTree()
    #plt.show()
    pass