from Node import Node


class BST:

    def __init__(self):
        self.root = None  # Root of the BTS

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return Node(key)  # Create new node

        if key < node.key:
            node.left = self._insert_recursive(node.left, key)  # Go Left
        else:
            node.right = self._insert_recursive(node.right, key)  # Go Right

        return node  # Return the modified node
