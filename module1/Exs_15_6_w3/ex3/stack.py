from node import LinkedList


class Stack(LinkedList):
    def __init__(self, capacity):
        self.count = capacity
        self.capacity = capacity
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def is_full(self):
        if self.size_of_ll() == self.capacity:
            return True
        else:
            return False

    def pop(self):
        if self.head is None:
            return

        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_data = current_node.next.data
        current_node.next = None

        return current_data

    def push(self, value):
        self.insert_at_end(value)

    def top(self):
        if self.head is None:
            return

        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        return current_node.next.data
