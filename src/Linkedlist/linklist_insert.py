class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

    def insertAt(self, prev_node, new_value):
        if prev_node is Node:
            print("Previous node seems to be empty")

        new_node = Node(new_value)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_value):
        new_value = Node(new_value)

        if self.head is None:
            self.head = new_value
            return

        last = self.head
        while(last.next):
            last = last.next

        last.next = new_value
    
    def deleteNode(self, key):

        temp = self.head

        # case 1
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return

        # case 2
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # case 3
        if (temp == None):
            return

        prev.next = temp.next

        temp = None

    def deletetotallist(self):

        curr = self.head

        while curr:
            prev = curr.next

            del curr.data

            curr = prev

    def printlist(self):
        tmp = self.head
        while(tmp):
            print(tmp.data)
            tmp = tmp.next


if __name__ == '__main__':
    llist = LinkedList()

    llist.append(3)
    llist.push(4)
    llist.push(5)
    llist.push(6)

    llist.printlist()

    