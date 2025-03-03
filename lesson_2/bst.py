from collections import deque

from Node import Node


class BST:

    def __init__(self):  # constructor
        self.root = None  # Root of the BTS

    def insert(self, node):
        if not isinstance(node, Node):  # checks if param passed is a Node() class
            raise TypeError("Expected a Node Object")

        self.root = self._insert_recursive(self.root, node)  # recursive function for node implementation

    def _insert_recursive(self, current_node, next_node):
        if current_node is None:  # return next_node as current node if none, node is none if root
            return next_node

        if next_node.key < current_node.key:
            current_node.left = self._insert_recursive(current_node.left, next_node)
        else:
            current_node.right = self._insert_recursive(current_node.right, next_node)

        return current_node

    def in_order_traversal(self, current):
        if current is None:  # return empty list if node is None. Node will be none if root
            return []

        # return bst in order: left node, parent node and right node. ascending order.
        return (self.in_order_traversal(current.left) +
                [current.key] +
                self.in_order_traversal(current.right))

    def pre_order_traversal(self, current_node):
        if current_node is None:  # if node is None return empty list, will also prevent the code from breaking once
            return []  # the recursion calls a non existing node

        # return bst: current node first then, left subtree and finally right subtree
        return [current_node.key] + self.pre_order_traversal(current_node.left) \
               + self.pre_order_traversal(current_node.right)

    def post_order_traversal(self, current_node):
        if current_node is None:  # if node is Node return empty list.
            return []

        # returns left subtree, right subtree and then current node
        return self.post_order_traversal(current_node.left) \
               + self.post_order_traversal(current_node.right) + [current_node.key]

    def level_order_traversal(self, current_node):
        if current_node is None:  # if node is Node return empty list.
            return []

        result = []
        queue = deque([current_node])  # First node(root) in the queue

        while queue:
            node = queue.popleft()  # remove node at the front of the queue
            result.append(node.key)  # Process the current node

            #  Add children node to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result
