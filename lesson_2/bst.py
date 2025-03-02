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

    def in_order_traversal(self, current):
        if current is None:
            return []

        # return bst in order: left node, parent node and right node. ascending order.
        return (self.in_order_traversal(current.left) +
                [current.key] +
                self.in_order_traversal(current.right))

    def pre_order_traversal(self, current_node):
        if current_node is None: # if node is None return empty list, will also prevent the code from breaking once the recursion calls a non existing node
            return []

        # return bst: current node first then, left subtree and finally right subtree
        return [current_node.key] + self.pre_order_traversal(current_node.left) \
               + self.pre_order_traversal(current_node.right)
