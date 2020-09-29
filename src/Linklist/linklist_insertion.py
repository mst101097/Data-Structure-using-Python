class Node:  # this class used for create a node for linkedlist
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList: # main class used for Single Linkedlist 
    def __init__(self):
        self.head = None
    # This method used for push an element in linklist
    def push(self,new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node
    # This method use for insert element in particular position 
    def InsertAt(self,pre_node,new_value):
        if pre_node is Node:
            print("List seems like empty")
        
        new_node = Node(new_value)
        new_node.next = pre_node.next
        pre_node.next = new_node
    # This element used for add an element in linkedlist at last
    def append(self,new_value):
        new_value = Node(new_value)

        if self.head is None:
            self.head = new_value
            return
        
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_value
    # This method used for  delete partcular node value 
    def deleteNode(self,key):
        temp =  self.head

        # CASE 1
        if(temp is not None):
            if(temp.data == key):
                self.head = temp.next
                temp = None
                return

        
        # CASE 2
        while(temp is not None):
            if(temp.data == key):
                break
            prev = temp
            temp = temp.next
        
        #Case 3
        if(temp == None):
            return

        prev.next =  temp.next
        temp = None
    # This method used for delete all element in linklist 
    def deleteall_linkedlist(self):
        curr = self.head
        while curr:
            prev = curr.next
            del curr.data
            
            curr = prev
    #This method used for print all data node from linked list
    def Printdata(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    # This method used for count node of linkedlist 
    def getcountNode(self,Node):
        if(not Node):
            return 0
        else:
            return 1 + self.getcountNode(Node.next)
        
    def getcount(self):
        return self.getcountNode(self.head)
    # This method used for  reverse linklist
    def Reverse_linklist(self):
        prev = None
        current = self.head

        while(current is not None):
            next = current.next
            current.next = prev
            prev = current   # Second type to writen code line ( prev,current = current , next) 
            current = next
        self.head = prev

if __name__=='__main__':
    llist = LinkedList()
    llist.push(3)
    llist.append(4)
    llist.append(5)
    # llist.InsertAt(2,4)
    print(llist.getcount())
    # llist.Printdata()
    # llist.deleteNode(5)
    #llist.deleteall_linkedlist()

  



    

