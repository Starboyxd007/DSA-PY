class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def insertAtFront(self, value):
        self.items.insert(0, value)

    def deleteAtFront(self):
        if self.isEmpty():
            raise Exception("Deque is empty")
        return self.items.pop(0)

    def insertAtEnd(self, value):
        self.items.append(value)

    def deleteAtEnd(self):
        if self.isEmpty():
            raise Exception("Deque is empty")
        return self.items.pop()

    def print(self):
        for i in self.items:
            print(i, end=" ")
        print()


dll = Deque()
dll.insertAtEnd(10)
dll.insertAtEnd(20)
dll.insertAtFront(5)
dll.print()