"""
Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""

from LinkedList import LinkedList

    def remove_duplicates(self, head):
        s = set()
        n = head
        while n.next_val is not None:
            if n.data_val in s:
                n = n.next_val.next_val
            else:
                s.add(n.data_val)
            n = n.next_val
        return head

    def remove_duplicates2(self, head):
        n = head
        while n.next_val is not None:
            m = n
            while m.next_val is not None:
                if n.data_val == m.next_val.data_val:
                    m.next_val = m.next_val.next_val
                else:
                    m = m.next_val
            n = n.next_val

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

    # Given only access to that node.
    def delete_middle_node(self, node):
        node.data_val = node.next_val.data_val
        node.next_val = node.next_val.next_val
        return True

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

    def add_first(self, head):
        node = Node("11")
        node.next_val = head
        return node

    def reverse_list(self, head):
        current = head
        while current.next_val is not None:
            node = current.next_val
            current.next_val = current.next_val.next_val
            node.next_val = head
            head = node
            node = node.next_val
        return head

    # is the same, forwards and backwards
    def palindrom(self, head):
        pass


if __name__ == "__main__":
    list_ = LinkedList()
    list_.head_val = Node("3")
    list_.append_to_tail(Node("4"))
    list_.append_to_tail(Node("6"))
    list_.append_to_tail(Node("7"))
    list_.append_to_tail(Node("8"))
    list_.append_to_tail(Node("9"))
    c = Node("1")
    list_.append_to_tail(c)
    list_.return_kth_to_last_element(list_.head_val, 3)
    list_.delete_middle_node(c)
    list_.reverse_list(list_.head_val)
    list_.add_first(list_.head_val)
    list_.printList(list_.reverse_list(list_.head_val))
