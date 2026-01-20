class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    # Insert at a specific position
    def insert_at_position(self, data, position):
        if position < 1:
            print("Position must be >= 1")
            return
        
        new_node = Node(data)
        if position == 1:
            self.insert_at_beginning(data)
            return
        
        current = self.head
        for _ in range(position - 2):
            if current.next is None:
                print("Position out of range")
                return
            current = current.next
        
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node

    # Search for an element
    def search(self, data):
        current = self.head
        position = 1
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

    # Delete from the beginning
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    # Delete from the end
    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next:
                current = current.next
            current.prev.next = None

    # Delete from a specific position
    def delete_at_position(self, position):
        if position < 1 or self.head is None:
            print("Invalid position or list is empty")
            return
        
        if position == 1:
            self.delete_from_beginning()
            return
        
        current = self.head
        for _ in range(position - 1):
            if current.next is None:
                print("Position out of range")
                return
            current = current.next
        
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev

    # Delete a specific element
    def delete_element(self, data):
        position = self.search(data)
        if position == -1:
            print(f"Element {data} not found")
        else:
            self.delete_at_position(position)

    # Display the list
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" <-> ".join(elements) if elements else "List is empty")

    # Display in reverse
    def display_reverse(self):
        if self.head is None:
            print("List is empty")
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.prev
        print(" <-> ".join(elements))


# Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()
    
    # Insert elements
    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)
    dll.insert_at_end(40)
    
    print("Original list:")
    dll.display()
    
    # Insert at beginning
    dll.insert_at_beginning(5)
    print("\nAfter inserting 5 at beginning:")
    dll.display()
    
    # Insert at position
    dll.insert_at_position(25, 4)
    print("\nAfter inserting 25 at position 4:")
    dll.display()
    
    # Search
    data = 25
    pos = dll.search(data)
    print(f"\nSearching for {data}: Position {pos}" if pos != -1 else f"\nElement {data} not found")
    
    # Delete from beginning
    dll.delete_from_beginning()
    print("\nAfter deleting from beginning:")
    dll.display()
    
    # Delete from end
    dll.delete_from_end()
    print("\nAfter deleting from end:")
    dll.display()
    
    # Delete at position
    dll.delete_at_position(2)
    print("\nAfter deleting at position 2:")
    dll.display()
    
    # Delete specific element
    dll.delete_element(25)
    print("\nAfter deleting element 25:")
    dll.display()
    
    # Display reverse
    print("\nList in reverse:")
    dll.display_reverse()
