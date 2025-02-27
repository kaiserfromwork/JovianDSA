from Node import Node


class BST:

    def __init__(self):
        self.root = None  # Root of the BTS

    def insert(self, node):
        if not isinstance(node, Node):
            raise TypeError("Expected a Node Object")

        self.root = self._insert_recursive(self.root, node)

    def _insert_recursive(self, current_node, next_node):
        if current_node is None:
            return next_node

        if next_node.key < current_node.key:
            current_node.left = self._insert_recursive(current_node.left, next_node)
        else:
            current_node.right = self._insert_recursive(current_node.right, next_node)

        return current_node
