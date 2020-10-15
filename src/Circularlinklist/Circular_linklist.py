class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Circular_linklist:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = Node(data)
        temp = self.head

        new_node.next = self.head

        if self.head is not None:
            while(temp.next != self.head):
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node 
        self.head = new_node
    
    def cprintlinklist(self):
        temp = self.head
        if self.head is not None:
            while(True):
                print(temp.data)
                temp = temp.next
                if temp == self.head:
                    break

    
    def delete(self,deleteval):
        current_node = self.head
        prev_node = None

        while current_node:
            # if current node data equal delete node and head node than loop will be enter this condition
            if current_node.data == deleteval and current_node.data == self.head:
                if current_node.next == self.head:
                    current_node = None
                    self.head = None
                    return
                else:
                    while current_node.next != self.head:
                        current_node = current_node.next
                    current_node.next = self.head.next
                    self.head = self.head.next
                    current_node = None
                    return
            # regular delete conditon if current node data meet in delete value
            elif current_node.data == deleteval:
                prev_node.next = current_node.next
                current_node = None
                return

            else:
                if current_node.next == self.head:
                    break

            prev_node = current_node
            current_node = current_node.next

    def countNode(self):
        current = self.head
        self.count =  self.count+1
        while(current.next != self.head):
            self.count = self.count + 1
            current = current.next
        print(self.count)

    def tocircular(self,head):
        start =  head
        while(head.next is not None):
            head = head.next
        head.next = start
        return start

cirlist = Circular_linklist()
cirlist.push(5)
cirlist.push(6)
cirlist.push(4)
cirlist.cprintlinklist()
cirlist.countNode()
# cirlist.delete(6)
# cirlist.cprintlinklist()

