#34,45,46,67,78,89,23,34
# 0, 1, 2, 3, 4, 5, 6, 7,

#(self.rear+1)%self.size == self.front

class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.rear = self.front = -1

    def enqueue(self,data):
        if ((self.rear+1)% self.size == self.front):
            print("Queue is Full")
            return
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear+1) % self.size
            self.queue[self.rear] = data
        print(self.queue)
        
        
    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty")
            return

        elif (self.front == self.rear):
            posval = self.queue[self.front]
            self.front = -1
            self.rear =  -1
            return posval

        else:
            posval = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return posval
        

q = CircularQueue(4)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
print(q.dequeue())


            
        

