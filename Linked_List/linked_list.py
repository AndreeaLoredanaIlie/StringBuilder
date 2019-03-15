"""
Implements a simple linked list
"""

class Node(object):

    def __init__(self, data):
        # Node element, stores data and "pointer" to next Node.
        self.data = data
        self.next = None

class LinkedList(object):

    def __init__(self):
        self.head = None

    def printList(self):
        temp_head = self.head
        while temp_head is not None:
            print(temp_head.data)
            temp_head = temp_head.next

    def iterateList(self):
        temp_head = self.head
        while temp_head is not None:
            yield temp_head.data
            temp_head = temp_head.next

    def append_to_tail(self, node):
        if self.head is None:
            # This is the first Node
            self.head = node
        else:
            temp_head = self.head
            while temp_head.next is not None:
                temp_head = temp_head.next
            temp_head.next = node

    def delete_a_node(self, node_val):
        node = self.head
        if node.data == 5:
            return self.head.next
        while node.next is not None:
            if node.data == 5:
                node = n.next.next
            node = node.next
        if not node:
            raise NoSuchNodeError

class NoSuchNodeError(Exception):
    pass


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append_to_tail(Node(1))
    linked_list.append_to_tail(Node(4))
    linked_list.append_to_tail(Node(6))
    linked_list.printList()
    print(linked_list)
