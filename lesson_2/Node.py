class Node:

    def __init__(self, key):
        self.key = key  # Store the value of this Node
        self.left = None  # Pointer to left child (smaller Node)
        self.right = None  # Pointer to right child (larger Node)

    def __repr__(self):
        return f'Node({self.key})'

    def __str__(self):
        return f'Node key: {self.key}, left child: {"No left child" if self.left is None else self.left.key}, ' \
               f'right child: {"No right child" if self.right is None else self.right.key}'