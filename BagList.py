from Bag_1 import Bag_1
from TNode import TNode
from simple_tree_node import SimpleTreeNode

class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class BagList(SimpleTreeNode):

    def __init__(self):
        self.head = None

    def is_Empty(self):
        return self.head == None

    def list_Insert(self, x):
        self.head = Node(data=x, next=self.head)

    def add_End(self, data):
        if not self.head:
            self.head = Node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data=data)

    def print_List(self):
        Node = self.head
        while Node != None:
            print(Node.data, end=" ")
            Node = Node.next

if __name__ == "__main__":

    myBag = Bag_1(1, False)
    nodo1 = TNode(0, 2)
    nodo2 = TNode(1, 5)
    nodo3 = TNode(2, 3)

    myBag.__setVertex1__(nodo1)
    myBag.__setVertex2__(nodo2)
    myBag.__setVertex3__(nodo3)

    myBag2 = Bag_1(1, False)
    nodo1 = TNode(5, 2)
    nodo2 = TNode(6, 5)
    nodo3 = TNode(7, 3)

    myBag2.__setVertex1__(nodo1)
    myBag2.__setVertex2__(nodo2)
    myBag2.__setVertex3__(nodo3)

    lista = BagList()

    lista.list_Insert(myBag)
    lista.list_Insert(myBag2)
    lista.print_List()