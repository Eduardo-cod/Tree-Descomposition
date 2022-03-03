from TNode import TNode
from simple_tree_node import SimpleTreeNode

class Bag_1(SimpleTreeNode):

    def __init__(self,node_id,is_bagged):
        super().__init__(node_id)
        self.bag_id = node_id
        self.bagged = is_bagged
        self.vertex1 = None
        self.vertex2 = None
        self.vertex3 = None
        self.parent = None

    def __setBagId__(self,node_id):
        self.bag_id = node_id

    def __getBagId__(self):
        return self.bag_id

    def __setVertex1__(self,xVertex1):
        self.vertex1 = xVertex1

    def __getVertex1__(self):
        return self.vertex1

    def __setVertex2__(self,xVertex2):
        self.vertex2 = xVertex2

    def __getVertex2__(self):
        return self.vertex2

    def __setVertex3__(self,xVertex3):
        self.vertex3 = xVertex3

    def __getVertex3__(self):
        return self.vertex3

    def __setParent__(self,xParent):
        self.parent = xParent

    def __getParent__(self):
        return self.parent

    # def __str__(self):
    #
    #     return f'({self.__getVertex1__()}, {self.__getVertex2__()}, {self.__getVertex3__()})'


if __name__ == "__main__":

    myBag = Bag_1(1,False)
    nodo1 = TNode(0,2)
    nodo2 = TNode(1,5)
    nodo3 = TNode(2,3)

    myBag.__setVertex1__(nodo1)
    myBag.__setVertex2__(nodo2)
    myBag.__setVertex3__(nodo3)

    print(myBag)