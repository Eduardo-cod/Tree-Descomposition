import networkx as nx
import random

class Graph:
    Node = None
    Tree = None

    def __init__(self, numNodes, isTree=True):
        self.Node = numNodes
        self.Tree = isTree
        if self.Tree:
            random.seed()
            seed = random.randint(1, 10)
            probability = random.random()
            G = nx.gnp_random_graph(numNodes, probability, seed, False)
            self.graph = nx.minimum_spanning_tree(G)
            self.setfakeDegree()
        else:
            self.graph = nx.fast_gnp_random_graph(numNodes, 0.3)

    def setfakeDegree(self):
        for i in range(0, len(self.graph.nodes())):
            self.graph.nodes[i]["fDegree"] = self.graph.degree(i)
            self.graph.nodes[i]["bagged"] = False

    def setFakeDegree(self, i, degree):
        self.graph.nodes[i]["fDegree"] = degree

    def getFakeDegree(self, i):
        return self.graph.nodes[i]["fDegree"]

    def getBagged(self, i):
        return self.graph.nodes[i]["bagged"]

    def setBagged(self, i):
        self.graph.nodes[i]["bagged"] = True

    def getNode(self, i):
        return self.graph.nodes[i]

    def returnGraph(self):
        return self.graph

if __name__ == '__main__':
    myGraph=Graph(10,True)
    print("Node:",myGraph.getNode(0))
    myGraph.setBagged(2) # just to test
    for i in range(0,len(myGraph.graph.nodes())):
        print("Degree:",myGraph.getFakeDegree(i), " isBagged: ",myGraph.getBagged(i))