"""
Write code to check if the list is circular.
Return the node at the beginning of the loop
An circular list is a linked list in which a node's next pointer point to an
earlier node, so as to make a loop in the linked list.
"""

from linked_list import LinkedList, Node


# Make use of two pointers (slow pointer and fast pointer)
# If slow pointer move two node for each slow pointer node
# they move one node closer on each turn
# Therefore they will meet
def loop_detection(list_):
    slow = list_
    fast = list_

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break

    # Error check - no meeting point
    if fast is None or fast.next is None:
        return False

    # If they move at the same pace, they must meet at loop start
    slow = list_
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return fast

if __name__ == "__main__":
    list_ = LinkedList()
    list_.head = Node("3")
    list_.append_to_tail(Node("1"))
    list_.append_to_tail(Node("2"))
    loop_node = Node("5")
    list_.append_to_tail(loop_node)
    list_.append_to_tail(Node("4"))
    list_.append_to_tail(loop_node)

    list_.printList()
    loop_detection(list_.head)
