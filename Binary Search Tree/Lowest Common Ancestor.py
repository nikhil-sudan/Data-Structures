# -*- coding: utf-8 -*-
"""
Created on Sat May 30 17:41:32 2020

@author: Nikhil Sudan
"""

"""
IDEA:
    Lowest common ancestor of 2 nodes(say n1 and n2) in a BST is a node which has both n1 and n2 as descendants(where we allow a node to be a descendant of itself)

INTRODUCTION:
    in this algorithm(recursive solution), we simply check if the two values v1 and v2 are on opposite site of current root node,
    if yes, we print the root node bcoz that will be the Lowest Common Ancestor.
    if not, that means they are on same side and there is some other common ancestor. So, we move to the next sub tree(and update the root) if both are on left side of current root node
    or we move to the next sub tree(and update the root) 
    now we check the position of n1 and n2 with this new root node of sub tree, like we did at start 
    this step is repeated again and again

"""

#creating a Node Class; 
#a node will be haivng info/value, 
#"left" that will store pointer to its left child and "right" that will store the pointer to its right child
class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 

#return the pointer to the lowest common ancestor node of the two nodes.
def lowestCommonAncestor(root, n1, n2):
    
    #if v1 and v2 are on opposite side of the current root, then return the root
    if(n1<=root.info and n2>=root.info or n1>=root.info and n2<=root.info):
        return(root)
        
    #if v1 and v2 both lie on the left side of current root node, then recursively calling function again in left sub tree to find lowest common ancestor
    elif(n1<root.info and n2<root.info):
        return(lowestCommonAncestor(root.left, n1, n2))
    
        #if v1 and v2 both lie on the right side of current root node, then recursively calling function again in right sub tree to find lowest common ancestor
    elif(n1>root.info and n2>root.info):
        return(lowestCommonAncestor(root.right, n1, n2))
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

# insert() method to perform insertion to form a binary search tree
    def insert(self, val):
        Node1=self.root
        
#checking if root exist. If does not exist, then we create the first node as root node
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
    
#creating an object of class-BinarySearchTree
tree = BinarySearchTree()

t = int(input())    #"t" denotes number of values to be inserted into the BST.

arr = list(map(int, input().split()))   # takes t inputs in one line and puts them in a array

#inserting each value one by one into the BST
for i in range(t):
    tree.insert(arr[i])


print("Choose any 2 values from: ", arr)
value1,value2= map(int, input().split())    #enter 2 values to find the loweset common ancestor

#print the value of Lowest common ancestor 
print("Lowest Common Ancestor of this BST is: ", lowestCommonAncestor(tree.root, value1, value2).info)
#inOrder(tree.root)

