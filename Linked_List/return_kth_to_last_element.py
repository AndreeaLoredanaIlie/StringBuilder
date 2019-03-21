"""
Write code to return kth to last element.
"""

from linked_list import LinkedList, Node


# Recursive way
# Iterate through the list
# When it hits the end, the method passes back a counter set to 0
# Each parent call increases by 1 the counter
def return_kth_to_last_element(self, head, k):
    if head.next_val == None:
        return 0
    index = self.return_kth_to_last_element(head.next_val, k) + 1
    if index == k:
        print('Head '+head.data_val)
    return index

if __name__ == "__main__":
    list_ = LinkedList()
    list_.head = Node("3")
    list_.append_to_tail(Node("1"))
    list_.append_to_tail(Node("2"))
    list_.append_to_tail(Node("4"))
    list_.append_to_tail(Node("1"))
    list_.append_to_tail(Node("2"))
    list_.append_to_tail(Node("4"))

    list_.printList()
    return_kth_to_last_element(list_.head, 4)
