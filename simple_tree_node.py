from simple_node import SimpleNode


class SimpleTreeNode(SimpleNode):
    """
    A class that represent a simple or basic tree node.
    """
    def __init__(self, node_id):
        """
        Init method for SimpleTreeNode
        :param node_id: (int) The vertex node_id
        """
        super().__init__(node_id)

        self.is_root = False
        self.is_leaf = False

    def __str__(self):
        """
        String representation of the SimpleTreeNode in the form:
            Id: node_id,    is root: True/False,    is leaf: True/False
        :return: (string) a string representation of SimpleTreeNode
        """
        return f"{super().__str__()}\tis root: {self.is_root},\tis leaf: {self.is_leaf}"