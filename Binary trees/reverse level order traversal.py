# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 00:46:40 2020

@author: Nikhil Sudan
"""
class Queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,value):
        self.items.insert(0, value)
    def dequeue(self):
        return self.items.pop()
    def is_Empty(self):
        return len(self.items)==0
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
    ########################################
    def __len__(self):
        return(self.size())
    def size(self):
        return(len(self.items))
    
class Stack:
    def __init__(self):
        self.items2=[]
    def push(self, value):
        self.items2.append(value)
    def pop(self):
        return self.items2.pop()
    def is_Empty(self):
        return(len(self.items2)==0)
    def __len__(self):
        return(self.size())
    def size(self):
        return(len(self.items2))
    
class Node:
    def __init__(self,value):
        self.value= value
        self.left=None
        self.right=None
    
class BinaryTree:
    def __init__(self, root):
        self.root=Node(root)
    def revLevelOrder(self, start):
        traverse=""
        if(start):
            queue=Queue()
            stack=Stack()
            queue.enqueue(start)
            while(len(queue)>0):
                node=queue.dequeue()
                #print(node.value)k
                if(node.right):
                    queue.enqueue(node.right)
                if(node.left):
                    queue.enqueue(node.left)
                stack.push(node)
        while(len(stack)>0):
            traverse+=str(stack.pop().value)+" - "
        return(traverse)
                
            
            

tree=BinaryTree(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.right.left=Node(6)
tree.root.right.right=Node(7)

print(tree.revLevelOrder(tree.root))

    