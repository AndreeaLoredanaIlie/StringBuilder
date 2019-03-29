"""
Implements a stack of plates.
Start a new stack when the previous stack exceeds a threshold.
"""
from stack import StackNode, Stack

class StackOfPlates(object):

    def __init__(self):
        self.set_of_stacks = []

    # If the poped element is the last in a stack
    # Then delete the stack
    def pop(self):
        import ipdb; ipdb.set_trace()
        last_stack = self.get_last_stack()
        if last_stack is None:
            raise EmptyStackException
        v = last_stack.pop()
        if last_stack.is_empty():
            self.set_of_stacks.pop()
        return v

    # We need to and check if the stack hits the limit,
    # then create a new stack.
    def push(self, item):
        last_stack = self.get_last_stack()
        if last_stack is not None and not last_stack.is_full():
            last_stack.push(item)
        else:
            new_stack = Stack()
            new_stack.push(item)
            self.set_of_stacks.append(new_stack)

    def get_last_stack(self):
        if len(self.set_of_stacks) == 0:
            return None
        return self.set_of_stacks[len(self.set_of_stacks)-1]

    def print_list(self):
        for item in self.set_of_stacks:
            import ipdb; ipdb.set_trace()
            item.print_list()

class EmptyStackException(Exception):
    pass

if __name__ == '__main__':
    stack_of_plates = StackOfPlates()
    stack_of_plates.push(1)
    stack_of_plates.push(4)
    stack_of_plates.push(6)
    stack_of_plates.push(3)
    stack_of_plates.push(2)
    stack_of_plates.push(5)
    stack_of_plates.push(7)
    stack_of_plates.pop()
    stack_of_plates.pop()
    stack_of_plates.print_list()
    print(stack_of_plates)
