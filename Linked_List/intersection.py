"""
Write code to check if the lists intersect.
Return the intersecting node
An intersection is defined based on the reference not on the value
"""

from linked_list import LinkedList, Node


# Determine if there is an intersaction (two intersecting lists have the same last node)
# Iterate to the end of the lists and compare the last node
def two_lists_intersect(list1, list2):
    tail1 = list1
    tail2 = list2
    len1 = 1
    len2 = 1
    import ipdb; ipdb.set_trace()
    while tail1.next is not None:
        len1 += 1
        tail1 = tail1.next

    while tail2.next is not None:
        len2 += 1
        tail2 = tail2.next

    if tail1 != tail2:
        return None
    import ipdb; ipdb.set_trace()
    # if the linked lists were the same lenght we could just traverse them at the same time
    # if not we ignore the excess nodes
    # the difference between them will tell us how much to drop off
    if len1 > len2:
        idx = 0
        while idx < len1-len2:
            list1 = list1.next
            idx += 1
    else:
        idx = 0
        while idx < len2-len1:
            list2 = list2.next
            idx += 1
    import ipdb; ipdb.set_trace()
    # we traverse on each list until the pointers are the same
    while list1 is not None:
        if list1 == list2:
            return list1
        list1 = list1.next
        list2 = list2.next

if __name__ == "__main__":
    list_1 = LinkedList()
    list_1.head = Node("3")
    list_1.append_to_tail(Node("4"))

    list_2 = LinkedList()
    list_2.head = Node("3")
    list_2.append_to_tail(Node("4"))
    list_2.append_to_tail(Node("6"))
    list_2.append_to_tail(Node("6"))
    list_2.append_to_tail(Node("6"))
    list_2.append_to_tail(Node("4"))
    list_2.append_to_tail(Node("3"))

    intersecting_node1 = Node("5")
    intersecting_node2 = Node("6")

    list_1.append_to_tail(intersecting_node1)
    #list_1.append_to_tail(intersecting_node2)

    list_2.append_to_tail(intersecting_node1)
    list_2.append_to_tail(intersecting_node2)

    list_1.printList()
    list_2.printList()
    two_lists_intersect(list_1.head, list_2.head)
