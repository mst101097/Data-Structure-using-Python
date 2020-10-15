class node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.key = key

class BST():
    def __init__(self,root = None):
        self.root = root

    def get_root(self):
        return self.root
    # this method use for insert a node in BST tree
    def insert(self,key):
        if self.root is None:
            self.root = node(key)
        else:
            self.insert_helper(self.root,key)

    #this is a helper method to insert in right position 
    def insert_helper(self,this_node,key):
        if this_node.key > key:
            if this_node.left is None:
                this_node.left = node(key)
            else:
                self.insert_helper(this_node.left,key)
        else:
            if this_node.right is None:
                this_node.right = node(key)
            else:
                self.insert_helper(this_node.right,key)
    #method find order to delete style
    def find_inorder_successor(self,this_node):
        myval = this_node
        while myval.left is not None:
            myval = myval.left
        return myval
    #method find order to delete style
    def find_inorder_predeuccessor(self,this_node):
        myval = this_node
        while myval.right is not None:
            myval = myval.right
        return myval
    # method use for delete node
    def delete_node(self,this_node,key):
        if this_node is None:
            return this_node
        if key < this_node.key:
            this_node.left = self.delete_node(this_node.left,key)
        elif key > this_node.key:
            this_node.right = self.delete_node(this_node.right,key)
        else: 
            # case where no child or 1 child
            if this_node.left is None:
                temp = this_node.right
                this_node = None
                return temp
            elif this_node.right is None:
                temp = this_node.left
                this_node = None
                return temp
            
            # case where 2 child and more than
            temp = self.find_inorder_successor(this_node.right)
            this_node.key = temp.key
            this_node.right = self.delete_node(this_node.right,temp.key)
        return this_node
    
    # method use for serach key in BST
    def search(self, this_node,key):
        if this_node is None:
            print('key is not found')
            return False
        elif this_node.key == key:
            print('key is found')
            return True
        elif key < this_node.key:
            self.search(this_node.left,key)
        else:
            self.search(this_node.right,key)

    def inorder(self, this_node):
        if this_node:
            self.inorder(this_node.left)
            print(this_node.key,end=" ")
            self.inorder(this_node.right)
    def preorder(self, this_node):
        if this_node:
            print(this_node.key,end=" ")
            self.preorder(this_node.left)
            self.preorder(this_node.right)
    def postorder(self, this_node):
        if this_node:
            self.postorder(this_node.left)
            self.postorder(this_node.right)
            print(this_node.key,end=" ")




        