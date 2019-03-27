"""
Implements a stack as a linked list
"""

class StackNode(object):

    def __init__(self, data):
        # Node element, stores data and "pointer" to next Node.
        self.data = data
        self.next = None

class Stack(object):

    def __init__(self):
        self.top = None

    # Remove the top item from the stack
    def pop(self):
        if self.top is None:
            raise EmptyStackException
        self.top = self.top.next

    # Add an item to the top of the stack
    def push(self, item):
        if self.top is None:
            self.top = StackNode(item)
        else:
            new_item = StackNode(item)
            new_item.next = self.top
            self.top = new_item

    def printList(self):
        temp_head = self.top
        while temp_head is not None:
            print(temp_head.data)
            temp_head = temp_head.next

    # Return the top item
    def peek(self):
        if self.top is None:
            raise EmptyStackException
        else:
            return self.top.data

    # Check if stack is empty
    def is_empty(self):
        return self.top is None

class EmptyStackException(Exception):
    pass


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(4)
    stack.push(6)
    stack.printList()
    print(stack)
