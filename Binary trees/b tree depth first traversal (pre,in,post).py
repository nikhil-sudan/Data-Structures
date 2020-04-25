# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 13:54:13 2020

@author: Nikhil Sudan
"""

class Node:
    def __init__(self, value):
        self.value=value
        self.right=None
        self.left=None
class BinaryTree:
    def __init__(self, root):
        self.root=Node(root)
    def preOrder(self, start, travStr):
        #Root, Left, Right = 1-2-4-5-3-6-7-
        if(start):
            travStr +=(str(start.value)+"-")
            travStr= self.preOrder(start.left, travStr)
            travStr= self.preOrder(start.right, travStr)
        return(travStr)
    
    def inOrder(self, start, travStr):
        # Left, Root, Right = 4-2-5-1-6-3-7-
        if(start):
            travStr= self.inOrder(start.left, travStr)
            travStr+=str(start.value)+"-"
            travStr=self.inOrder(start.right, travStr)
        return(travStr)
    
    def postOrder(self, start, travStr):
        # Left, Right, Root = 4-5-2-6-7-3-1-
        if(start):
            travStr = self.postOrder(start.left, travStr)
            travStr = self.postOrder(start.right, travStr)
            travStr +=str(start.value)+"-"
        return(travStr)
            

        
tree= BinaryTree(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.right.left=Node(6)
tree.root.right.right=Node(7)

# print(tree.preOrder(tree.root, ""))
# print(tree.inOrder(tree.root, ""))
print(tree.postOrder(tree.root, " "))




