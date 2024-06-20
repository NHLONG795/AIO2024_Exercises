from node import LinkedList, Node


class Queue(LinkedList):
    def __init__(self, capacity):
        self.count = capacity
        self.capacity = capacity
        self.front_pointer = None
        self.rear_pointer = None

    def is_empty(self):
        if self.front_pointer is None and self.rear_pointer is None:
            return True
        else:
            return False

    def enqueue(self, data):
        # NOTE: init create new node
        new_node = Node(data)
        up_to_date_node = self.rear_pointer

        if self.front_pointer is None and self.rear_pointer is None:
            self.front_pointer = new_node
            self.rear_pointer = new_node
        else:
            up_to_date_node.next = new_node
            self.rear_pointer = new_node

    def dequeue(self):
        if self.front_pointer and self.rear_pointer is None:
            return
        # NOTE: if both of them point to None its mean just only one node
        # rest on list
        elif self.front_pointer.next is None and self.rear_pointer.next is None:
            self.front_pointer = self.front_pointer.next
            self.rear_pointer = self.rear_pointer.next

        # NOTE: remove node on a head
        node_want_to_remove = self.front_pointer
        self.front_pointer = node_want_to_remove.next
        node_want_to_remove.next = None

    def front(self):
        return self.front_pointer

    def is_full(self):
        current_node = self.front_pointer
        count = 0
        while current_node:
            current_node = current_node.next
            count += 1

        if count == self.capacity:
            return True
        else:
            return False

    def print_queue(self):
        current_node = self.front_pointer
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
