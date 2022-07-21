class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next # pointer to the next element


class LinkedList:
    def __init__(self):
        self.head = None  # points to the head of the linked list

    def insert_at_beginning(self, data):
        node = Node(data, self.head) # NEXT element will be the self.head, which refers to the current head
        self.head = node # new head is updated to be the new node
                            # think it like a snake, start of the linkedlist is always a head
                            # always treat head as a node, and it has an object of class Node,
                            # so it has data and next attribute

    def print(self):
        if self.head is None: #blank linked list
            print("Linked List is empty")
            return

        itr = self.head #iterator
        llstr = '' #linked list string

        while itr: # while not blank
            llstr += str(itr.data) + ' --> '
            itr = itr.next

        print(llstr)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(47)
    ll.print()
    pass
