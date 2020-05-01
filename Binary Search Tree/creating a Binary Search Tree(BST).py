# -*- coding: utf-8 -*-
"""
Created on Fri May  1 18:50:33 2020

@author: Nikhil Sudan
"""
"""
IDEA:
    Binay search tree is a tree having following properties:
    The left subtree of a node contains only nodes with keys lesser than the node’s key.
    The right subtree of a node contains only nodes with keys greater than the node’s key.
    The left and right subtree each must also be a binary search tree.

INTRODUCTION:
    in this algorithm, we first check if the root exist, otherwise we create a node and make it root node for BST
    for each first value to be inserted:
          if that value is smaller than the parent node then we insert to LHS
          otherwise we make it the right node of the parent

"""

#creating a Node Class 
class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 


#return list of nodes in PRE-ORDER traversal (root,left,right)
def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
#return list of nodes in IN-ORDER  traversal (left,root,right)
def inOrder(root):
    if root == None:
        return
    inOrder(root.left)
    print (root.info, end=" ")
    inOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

# insert() method to perform insertion to form a binary search tree
    def insert(self, val):
        Node1=self.root
        
#checking if root exist. If does not exist, then we create root node
        if(Node1==None):  
            self.root=Node(val)

#finding the right position for the node and inserting it
        else:
            while(Node1):
                #if value of the node is smaller than the parent than we move to LHS sub tree
                if(val<Node1.info):
                    if(Node1.left):
                        Node1=Node1.left
                    else:
                        Node1.left=Node(val)
                        break
                #if value of the node is greater than the parent than we move to RHS sub tree
                else:
                    if(Node1.right):
                        Node1=Node1.right
                    else:
                        Node1.right=Node(val)
                        break
        return tree.root

tree = BinarySearchTree()

t = int(input())    #t denotes number of values to be inserted into the BST.

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

#print("pre-order traversal of a BST is: ", end="")
#preOrder(tree.root)  #prints pre-order traversal traveral of the BST


print("in-order traversal of a BST is: ", end="")
inOrder(tree.root)

"""
    ***NOTE: in-order traversal of a BST gives values in increasing order
"""