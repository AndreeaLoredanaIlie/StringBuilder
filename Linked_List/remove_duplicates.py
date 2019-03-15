"""
Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""

from linked_list import LinkedList, Node

# Make use of temporary set that keeps track oll tha values seen so far
# Worst case running time is O(n)
def remove_duplicates_with_set(n):
    s = set()
    #n = head
    previous = None
    while n is not None:
        import ipdb; ipdb.set_trace()
        if n.data in s:
            previous.next = n.next
        else:
            s.add(n.data)
            previous = n
        n = n.next

# Uses two pinters to keep trak of the current location
# Worst case running time is O(n)
def remove_duplicates_without_set(head):
    n = head
    while n.next is not None:
        m = n
        while m.next is not None:
            if n.data == m.next.data:
                m.next = m.next.next
            else:
                m = m.next
        n = n.next

if __name__ == "__main__":
    list_ = LinkedList()
    list_.head = Node("3")
    list_.append_to_tail(Node("4"))
    list_.append_to_tail(Node("6"))
    list_.append_to_tail(Node("4"))
    list_.append_to_tail(Node("8"))
    list_.append_to_tail(Node("9"))
    c = Node("1")
    list_.append_to_tail(c)
    print("{}".format(list_))
    list_.printList()
    remove_duplicates_without_set(list_.head)
    print("{}".format(list_))
    list_.printList()
