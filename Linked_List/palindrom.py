"""
Write code to check if a linked list is a palindrom
A list is a palindrom if the list is the same forwards and backwards
"""

from linked_list import LinkedList, Node

# Make use of temporary array that keeps half of the linked_list
# Iterate throught the list using running technique (fast pointer, slow pointer)
# At each step we add the data from the slow runner into an array
# When the fast pointer hits the end of the list, the slow runner will have reached the middle of the list
def check_if_linked_list_is_palindrom(n):
    temp_half = []
    node1 = n
    node2 = n
    idx1 = 0
    import ipdb; ipdb.set_trace()
    while node1.next is not None:
        if node1.next.next is not None:
            node1 = node1.next.next
            idx1 += 1
        else:
            node1 = node1.next
        temp_half.append(node2.data)
        node2 = node2.next

    # Handle the case where the length of the linked list is odd.
    # Has odd numbers of elements, so skip the middle node
    idx = 0
    if idx1 % 2 == 1:
        node2 = node2.next
    # Iterate through the rest of the list
    # At each step we compare the items from the array backwards to forwards to the node
    while node2 is not None:
        if temp_half[len(temp_half)-idx-1] != node2.data:
            return False
        node2 = node2.next
        idx += 1
    return True

if __name__ == "__main__":
    list_ = LinkedList()
    list_.head = Node("3")
    list_.append_to_tail(Node("4"))
    list_.append_to_tail(Node("6"))
    list_.append_to_tail(Node("6"))
    list_.append_to_tail(Node("6"))
    list_.append_to_tail(Node("4"))
    list_.append_to_tail(Node("3"))
    list_.printList()
    check_if_linked_list_is_palindrom(list_.head)
