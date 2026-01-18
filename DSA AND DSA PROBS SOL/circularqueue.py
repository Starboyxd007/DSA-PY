class CircularQueue:
    def __init__(self, size):
        self.size = size
        #This Will Create A Circular Queue of Given size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
    #Checks if the CirQue Is Full
    def isFull(self):
        return (self.rear + 1) % self.size == self.front
    
    #Checks if the CirQue Is Empty
    def isEmpty(self):
        return self.front == -1

    #Adds An Element To The CirQue
    def enqueue(self, data):
        if self.isFull():
            print("Circular Queue is full")
            return
        elif self.isEmpty():
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data
    

    #Removes An Element From The CirQue
    def dequeue(self):
        if self.isEmpty():
            raise Exception("Circular Queue is Empty")
        elif self.front == self.rear:
            data = self.queue[self.front]
            self.front = -1
            self.rear = -1
        else:
            print(self.queue[self.front])
            self.front = (self.front + 1) % self.size

    def printQueue(self):
        if self.isEmpty():
            print("Circular Queue is Empty")
            return
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()




dll = CircularQueue(5)
dll.enqueue(10)
dll.enqueue(20)
dll.enqueue(30)
dll.enqueue(40)
dll.enqueue(50)
dll.dequeue()
dll.dequeue()
dll.enqueue(5)
dll.enqueue(8)
dll.enqueue(5)
dll.printQueue() 