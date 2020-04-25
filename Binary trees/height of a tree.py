# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 16:54:51 2020

@author: Nikhil Sudan
"""

# IDEA:
#     height of a tree is the max depth from the root

    
# INTRODUCTION:
#     recursive method to find height
#     we find height of left and right subtree of a node 
#     and we return the max of the two values    

class Node:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
        
class BinaryTree:
    def __init__(self, root):
        self.root=Node(root)
    
    def height(self, start):
        if (start==None):
            return -1
        self.left_height=self.height(start.left)
        self.right_height=self.height(start.right)
        
        return (1+max(self.left_height, self.right_height))

tree=BinaryTree(1)                          #        1
tree.root.left=Node(2)                      #      /   \
tree.root.right=Node(3)                     #     2     3
tree.root.left.left=Node(4)                 #    / \   / \
tree.root.left.right=Node(5)                #   4   5 6   7
tree.root.right.left=Node(6)                    
tree.root.right.right=Node(7)

print("height of the tree is: ",tree.height(tree.root))     #prints- "height of the tree is:  2"