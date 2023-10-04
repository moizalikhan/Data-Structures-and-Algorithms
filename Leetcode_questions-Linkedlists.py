# Reversal of Linked_lists
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Save the next node
            current.next = prev      # Reverse the pointer
            prev = current           # Move prev to the current node
            current = next_node     # Move current to the next node
        self.head = prev           # Update the head to the last node

# Example usage:
my_linked_list = LinkedList()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
print("Original Linked List:")
my_linked_list.display()
my_linked_list.reverse()
print("Reversed Linked List:")
my_linked_list.display()