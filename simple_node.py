class SimpleNode:
    """
    A class that represents a simple or basic node of a graph.
    """
    def __init__(self, node_id):
        """
        Init method for the SimpleNode
        :param node_id (int): The vertex node_id.
        """
        self.node_id = node_id

    def __str__(self):
        """
        String representation of the SimpleNode in the form: "Id: node_id"
        :return:(string) Returns a string representation of the SimpleNode
        """
        return f"Id: {self.node_id}"