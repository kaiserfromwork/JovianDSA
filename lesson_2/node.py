class Node:

    def __init__(self, key):
        self.key = key  # Store the value of this Node
        self.left = None  # Pointer to left child (smaller Node)
        self.right = None  # Pointer to right child (larger Node)
