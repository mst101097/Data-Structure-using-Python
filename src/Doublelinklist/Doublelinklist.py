import gc
class Node:   #This is a node class used for node create 
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev =  None

    
class Doublelinklist:
    def __init__(self):
        self.head = None

# This is the Push method in Doublelinklist which is push the value in head
    def push(self,data):
        new_node = Node(data)

        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

# This is the insert method which is used for insert particular node 
    def insertAfter(self,prev_node,data):
        if prev_node is None:
            print('Prevnode cannot be none')

        new_node = Node(data)
        
        new_node.next  = prev_node.next
        prev_node.next = new_node

        if new_node.next is not None:
            new_node.next.prev = new_node
# This method using for add element in last
    def addtolast(self,new_value):
        new_node = Node(new_value)
        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node

        last = self.head
        while last is not None:
            last = last.next

        last.next = new_node
        new_node.prev = last
        return

    def deletenode(self,key):
        if self.head is None or key is None:
            return
        # case 1 if key is on head Node
        if self.head == key:
            self.head = key.next

        #case 2
        if key.next is not None:
            key.next.prev = key.prev
        # CASE 3
        if key.prev is not None:
            key.prev.next = key.next
        
        gc.collect()



# '''This method using for print Double linklist data this method only when user give head node'''
    def printdlist(self):
        node = self.head
        while(node is not None):
            print(node.data,end=" ")
            node = node.next

    


if __name__ == "__main__":
    dbl = Doublelinklist()
    dbl.push(5)
    dbl.push(6)

    dbl.printdlist()


    







