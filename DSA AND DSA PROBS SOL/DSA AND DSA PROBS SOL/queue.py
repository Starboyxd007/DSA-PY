class Queue:
    def __init__(self):
        self.item = []
    def isEmpty(self):
        return len(self.item) == 0
    
    def insert(self, value):
        self.item.append(value)

    def delete(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        self.item.pop(0)

    def print(self):
        for i in self.item:
            print(i, end = " ")



dll = Queue()
dll.insert(10)
dll.insert(20)
dll.insert(30)
dll.insert(40)
dll.insert(50)
dll.delete()
dll.delete()
dll.delete()
dll.delete()
dll.delete()
dll.delete()
dll.print()