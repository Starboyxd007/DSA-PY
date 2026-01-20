class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")
            return None
        
    def print_stack(self):
        print(self.items)
dll = Stack()
dll.push(10)
dll.push(20)
dll.push(30)
dll.pop()
dll.pop()
dll.pop()
dll.print_stack()