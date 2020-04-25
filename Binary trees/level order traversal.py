# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 23:13:08 2020

@author: Nikhil Sudan
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
#DID  UNDERSTAND THIS: bcoz of line
    def __len__(self):
        return(self.size())
    def size(self):
        return (len(self.items))
            
class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self, root):
        self.root=Node(root)
    def leveOrder(self,start):
        traversal=""
        if(start):
            queue=Queue()
            queue.enqueue(start)
            while(len(queue)>0):
                traversal+=str(queue.peek())
                node=queue.dequeue()
                if(node.left):
                    queue.enqueue(node.left)
                if(node.right):
                    queue.enqueue(node.right)
            return(traversal)
                
        
        
tree= BinaryTree(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.right.left=Node(6)
tree.root.right.right=Node(7)

print(tree.leveOrder(tree.root))