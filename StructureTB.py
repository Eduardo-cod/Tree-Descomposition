from TNode import TNode
from Graph import Graph
import networkx as nx

class StructureTB:

    def __init__(self):
        self.sampleTree = None
        self.headNode = None
        self.Q1 = []
        self.Q2 = []

    def fillQueues(self,treeGraph):
        allNodes=treeGraph.nodes
        for i in range(len(allNodes)):
            xnode:TNode=allNodes[i]
            #print(node['data'])
            #tempDegree=node['fDegree']
            tempDegree = xnode['data'].__getvDegree__()
            #xID = xnode.__getvDegree__()
            if tempDegree==1:
                self.Q1.append(xnode['data'])
            if tempDegree==2:
                self.Q2.append(xnode['data'])

    def dequeue(self, auxQ):
        return auxQ.pop(0)
        # return self.Q1.pop(0)

    def enqueue(self, v: TNode):
        tempDegree = v['data'].volatileDegree
        if tempDegree == 1:
            self.Q1.append(v['data'])
            return self.Q1
        if tempDegree == 2:
            self.Q2.append(v['data'])
            return self.Q2
        return self.Q1

    def replaceSampleTree(self,xSampleTree,xNode:TNode):
        """
        Let T = (V_T, E_T) be a NetworkX tree graph and w
        :return: A tree graph G with nodes as KNodes as above.
        """
        G = nx.Graph()
        nodes_dict = dict()

        for index in range(0, len(list(xSampleTree.nodes))):
            node = list(xSampleTree.nodes)[index]
            node = TNode(index,xSampleTree.degree[node])
            if xNode._node_id==index:
                node=xNode
            G.add_node(index, data=node)
        for edge in xSampleTree.edges:
            u_id = edge[0]
            v_id = edge[1]
            #u_id = nodes_dict[edge[0]]
            #v_id = nodes_dict[edge[1]]

            G.add_edge(u_id, v_id)

            # H = nx.Graph()
            # for node in G.nodes:
            #     nuevo_nodo = list(node)
            #     H.add_node(nuevo_nodo)

        return G

    def _tree_2_KGraph(self, T: nx):
        """
        Let T = (V_T, E_T) be a NetworkX tree graph and w
        :return: A tree graph G with nodes as KNodes as above.
        """
        G = nx.Graph()
        nodes_dict = dict()

        for index in range(0, len(list(T.nodes))):
            node = list(T.nodes)[index]
            node = TNode(index,T.degree[node])
            #if type(node) == tuple:  # This is true at least for Junction trees
             #   node = KNode(index,T.degree[node])
            #nodes_dict[node] = index
            G.add_node(index, data=node)

        for edge in T.edges:
            u_id = edge[0]
            v_id = edge[1]
            #u_id = nodes_dict[edge[0]]
            #v_id = nodes_dict[edge[1]]

            G.add_edge(u_id, v_id)

            # H = nx.Graph()
            # for node in G.nodes:
            #     nuevo_nodo = list(node)
            #     H.add_node(nuevo_nodo)

        return G

    def extract_Single(self, G, v):
        for i in G.neighbors(v._node_id):
            node = list(G.nodes)[i]
            node = TNode(i,G.degree[node])  # By default it is false the baged property for all nodes
            if node._baged is False:
                return node

    def decreaseDegree(self, G,v, curDegree):
        allNodes = G.nodes
        for i in range(len(allNodes)):
            node: TNode = allNodes[i]
            if node['data']._node_id == v._node_id:
                 newDegree = curDegree - 1
                 G.nodes[i]["volatileDegree"]=newDegree
                 return newDegree

    def printQueue(self, Q=[]):
        for x in range(0, len(Q)):
            print(Q[x])

if __name__ == "__main__":
    G = Graph(10,True)
    T = StructureTB()
    print(T.printQueue(T.Q1))
    pass