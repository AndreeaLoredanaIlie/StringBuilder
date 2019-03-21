"""
Two numbers represented by a linked list,
where each node contains a single digit.
The digits are stored in reverse order,
such that the 1's digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list
"""

from linked_list import LinkedList, Node


# two numbers represented by linked lists where each node contains a single digit
# the digits are stored in reverse order
def sum_lists(self, head1, head2, carry):
    if head1 is None and head2 is None and carry == 0:
        return None
    value = int(carry)
    if head1 is not None:
        value += int(head1.data_val)
    if head2 is not None:
        value += int(head2.data_val)

    node = Node(value % 10)
    node.next = self.sum_lists(
        head1.next_val if head1.next_val is not None else None,
        head2.next_val if head2.next_val is not None else None,
        1 if value > 10 else 0)
    return node

if __name__ == "__main__":
    list_1 = LinkedList()
    list_1.head = Node("4")
    list_1.append_to_tail(Node("5"))
    list_1.append_to_tail(Node("6"))

    list_2 = LinkedList()
    list_2.head = Node("3")
    list_2.append_to_tail(Node("1"))
    list_2.append_to_tail(Node("2"))

    list_1.printList()
    list_2.printList()
    return_kth_to_last_element(list_1.head, list_2.head)
