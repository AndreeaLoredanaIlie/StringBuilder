"""
Write code to delete a node in the middle of a singly linked list,
given only access to that node.
"""

from linked_list import LinkedList, Node


# Copy the data from the next node over to the current node,
# and then to delete the next node
def delete_middle_node(self, node):
    node.data_val = node.next_val.data_val
    node.next_val = node.next_val.next_val
    return True

if __name__ == "__main__":
    list_ = LinkedList()
    list_.head = Node("3")
    node = Node("4")
    list_.append_to_tail(Node("1"))
    list_.append_to_tail(Node("2"))
    list_.append_to_tail(node)
    list_.append_to_tail(Node("1"))
    list_.append_to_tail(Node("2"))
    list_.append_to_tail(Node("4"))

    list_.printList()
    delete_middle_node(node)
