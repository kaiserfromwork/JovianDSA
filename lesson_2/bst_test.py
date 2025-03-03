from bst import BST
from Node import Node


my_bst = BST()
print(my_bst.in_order_traversal(None))

node01 = Node(5)
node02 = Node(3)
node03 = Node(7)
node04 = Node(2)
node05 = Node(4)
node06 = Node(8)
node07 = Node(6)

my_bst.insert(node01)
my_bst.insert(node02)
my_bst.insert(node03)
my_bst.insert(node04)
my_bst.insert(node05)
my_bst.insert(node06)
my_bst.insert(node07)

print(node01)
print(node02)
print(node03)
print(node04)
print(node05)

print(  )
print(f'In-order Traversal: {my_bst.in_order_traversal(node01)}')
print(f'Pre-order Traversal: {my_bst.pre_order_traversal(node01)}')
print(f'Post-order Traversal: {my_bst.post_order_traversal(node01)}')
print(f'Level-order Traversal: {my_bst.level_order_traversal(node01)}')
# print(my_bst.in_order_traversal(node02))
# print(my_bst.in_order_traversal(node03))
# print(my_bst.in_order_traversal(node04))
# print(my_bst.in_order_traversal(node05))

