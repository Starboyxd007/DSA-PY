class ArrayDSA:
    def __init__(self):
        self.arr = []

    # Display array
    def display(self):
        print(self.arr)

    # Insert at end
    def insert_end(self, value):
        self.arr.append(value)

    # Insert at front
    def insert_front(self, value):
        self.arr.insert(0, value)

    # Insert at any index
    def insert_at_index(self, index, value):
        if index < 0 or index > len(self.arr):
            print("Invalid Index")
            return
        self.arr.insert(index, value)

    # Insert at middle
    def insert_middle(self, value):
        mid = len(self.arr) // 2
        self.arr.insert(mid, value)

    # Delete from end
    def delete_end(self):
        if not self.arr:
            print("Array is empty")
            return
        self.arr.pop()

    # Delete from front
    def delete_front(self):
        if not self.arr:
            print("Array is empty")
            return
        self.arr.pop(0)

    # Delete at any index
    def delete_at_index(self, index):
        if not self.arr:
            print("Array is empty")
            return
        if index < 0 or index >= len(self.arr):
            print("Invalid Index")
            return
        self.arr.pop(index)

    # Delete from middle
    def delete_middle(self):
        if not self.arr:
            print("Array is empty")
            return
        mid = len(self.arr) // 2
        self.arr.pop(mid)


a = ArrayDSA()

a.insert_end(10)
a.insert_end(20)
a.insert_end(30)
a.display()

a.insert_front(5)
a.display()

a.insert_middle(15)
a.display()

a.insert_at_index(2, 12)
a.display()

a.delete_end()
a.display()

a.delete_front()
a.display()

a.delete_middle()
a.display()

a.delete_at_index(1)
a.display()
