class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None  # points to the head of the linked list

    def print_forward(self):
        itr = self.head
        if itr.next is None:
            print("Linked List empty")
            return
        llstr = 'Forward Linked List is: '

        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)

    def print_backward(self):
        itr = self.head
        if itr.next is None:
            print("Linked List empty")
            return
        llstr ='Reversed Linked List is: '

        last_node = self.get_last_node()
        itr = last_node
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.prev
        print(llstr)


    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def insert_at_beginning(self, data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
            return
        else:
            node = Node(data, self.head, None)
            self.head.prev = node #### please take note
            self.head = node

    def insert_at_the_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        node = itr
        itr.next = Node(data, None, node)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(6)
    ll.insert_at_beginning(7)
    ll.insert_at_beginning(8)
    ll.insert_at_beginning(9)

    ll.print_forward()
    ll.print_backward()
    pass