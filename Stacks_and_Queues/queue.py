"""
Implements a queue as a linked list
"""

class QueueNode(object):

    def __init__(self, data):
        # Node element, stores data and "pointer" to next Node.
        self.data = data
        self.next = None

class Queue(object):

    def __init__(self):
        self.last = None
        self.first = None

    # Remove the first item from the stack
    def remove(self):
        if self.first is None:
            raise EmptyQueueException
        self.first = self.first.next
        if self.first is None:
            self.last = None

    # Add an item to the last of the stack
    def add(self, item):
        node = QueueNode(item)
        if self.last is not None:
            node.next = self.last
        self.last = node
        if self.first is None:
            self.first = self.last

    def printList(self):
        temp_head = self.first
        while temp_head is not None:
            print(temp_head.data)
            temp_head = temp_head.next

    # Return the top of the queue
    def peek(self):
        if self.first is None:
            raise EmptyQueueException
        else:
            return self.first.data

    # Check if queue is empty
    def is_empty(self):
        return self.first is None

class EmptyQueueException(Exception):
    pass


if __name__ == '__main__':
    queue = Queue()
    queue.add(1)
    queue.add(4)
    queue.add(6)
    queue.printList()
    print(queue)
