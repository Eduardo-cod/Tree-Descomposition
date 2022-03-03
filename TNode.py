import Graph

class TNode:

    def __init__(self, node_id, volatileDegree):
        self._node_id = node_id
        self._volatileDegree = volatileDegree
        self._baged = False

    def _getId_(self):
        return self._node_id

    def __getvDegree__(self):
        return self._volatileDegree

    def __getBaged__(self):
        return self._baged

    def __setBaged__(self):
        self._baged=True

    def __setvDegree__(self,volatileDegree):
        self._volatileDegree=volatileDegree

    def __getvDegree__(self):
        return self._volatileDegree

    def __str__(self):
        """
        String representation of the SimpleNode in the form: "Id: node_id"
        :return:(string) Returns a string representation of the SimpleNode
        """
        return f"[node_id: {self._node_id}, volatileDegree: {self._volatileDegree}, baged: {self._baged}]"

if __name__ == "__main__":
    myKNode=TNode(1,5)
    newNode:TNode=myKNode
    print(newNode)
    newNode.__setBaged__()
    tempDegree=newNode.__getvDegree__()-1
    newNode.__setvDegree__(tempDegree)
    print(newNode)
    
    print("##################################################")

    myGraph = Graph
    G = myGraph.Graph(10,True).returnGraph()
    node = list(G.nodes)
    for xNode in node:
        node = TNode(xNode, G.degree[xNode])
        newNode:TNode=node
        print(newNode)