"""
Implements a stack that has a function min which returns the minimum element
"""
import sys

class StackNode(object):

    def __init__(self, data):
        # Node element, stores data and "pointer" to next Node.
        self.data = data
        self.next = None
        self.min = sys.maxsize

class Stack(object):

    def __init__(self):
        self.top = None

    def min(self):
        return self.peek().min

    # Remove the top item from the stack
    def pop(self):
        if self.top is None:
            raise EmptyStackException
        self.top = self.top.next

    # Add an item to the top of the stack
    def push(self, item):
        if self.top is None:
            self.top = StackNode(item)
            self.top.min = item
        else:
            new_item = StackNode(item)
            new_item.next = self.top
            min_temp = self.top.min
            self.top = new_item
            if min_temp > item:
                self.top.min = item
            else:
                self.top.min = min_temp

    def print_list(self):
        temp_head = self.top
        while temp_head is not None:
            print(temp_head.data)
            temp_head = temp_head.next

    # Return the top item
    def peek(self):
        if self.top is None:
            raise EmptyStackException
        else:
            return self.top

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
    stack.print_list()
    stack.min()
    print(stack)
