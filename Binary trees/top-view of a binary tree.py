# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 17:09:25 2020

@author: Nikhil Sudan
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 15:56:36 2020

@author: Nikhil Sudan
"""

"""
IDEA:
    it is set of nodes visible when the tree is viewed from the top
    or the set of nodes who dont have any node above it
"""
"""
INTRODUCTION:
    -in this method, we iterate through the tree in level order
    -For that we find the horizontal distance of each node wrt to root (-ve for LHS and +ve for RHS and 0 for root )
    -for every node we check if there was any node before above it():
    -we also maitain 2 variables to tell us the max distance we have moved to both side
        for eg: for node-5 horizontal distance is 0(root->left->right)
        but we have already reached -1 horizontal distance(node-2), so of course this node is under some node. 
        so we dont include it in the final list of nodes
              1(0)
          /       \
      2(-1)       3(1)
    /     \      /   \
  4(-2)   5(0) 6(0)   7(2)
"""
class Queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.insert(0, item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return(len(self.items))==0
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
#   modifying len() function to return size of object of class Queue
    def __len__(self):
        return(self.size())
    def size(self):
        return (len(self.items))

class Node:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=0
        self.horizon=0

left_extreme=0
right_extreme=0
parent_horizon=0      
class BinaryTree:
    
    def __init__(self, root):
        self.root=Node(root)
        
        
    def topView(self, start):
        global left_extreme
        global right_extreme
        traversal=""
        
        if(start):
            queue=Queue()                       #initialised a object of Queue class
            queue.enqueue(start)
            traversal+=str(start.value)+"-"
            while(len(queue)>0):
                node=queue.dequeue()
                parent_horizon=node.horizon
                print("activr node",node.value, " horizon: ",node.horizon)
                print(left_extreme,"-", right_extreme)
                if(node.horizon<left_extreme):
                    traversal+=str(node.value)+"-"
                    left_extreme=node.horizon
                elif(node.horizon>right_extreme):
                    traversal+=str(node.value)+"-"
                    right_extreme=node.horizon
                if(node.left):
                    node.left.horizon=parent_horizon-1
                    queue.enqueue(node.left)
                if(node.right):
                    node.right.horizon=parent_horizon+1
                    queue.enqueue(node.right)
                
            return(traversal)       #returns string of nodes (level order)
        
        """
            if in case u need to print in left to right order
            create dictionary where KEY=node value and VALUE= horizontal distance
            sort the dictionary on the basis of VALUES and print keys
            CODE BELOW:
        dict1=sorted(dict1.items(), key = lambda kv:(kv[1], kv[0])) 
        for i in dict1:
            print(i[0], end=" ")
        """

tree=BinaryTree(1)                          #        1          
tree.root.left=Node(2)                      #      /   \
tree.root.right=Node(3)                     #     2     3
tree.root.left.left=Node(4)                 #    / \   / \
tree.root.left.right=Node(5)                #   4   5 6   7
tree.root.right.left=Node(6)                    
tree.root.right.right=Node(7)
            
# tree=BinaryTree(1)                            #        1
# tree.root.right=Node(2)                       #         \
# tree.root.right.right=Node(5)                 #          2
# tree.root.right.right.left=Node(3)            #           \
# tree.root.right.right.right=Node(6)           #            5
# tree.root.right.right.left.right=Node(4)      #          /   \
                                                #         3     6.
#                                                                 4

print(tree.topView(tree.root))