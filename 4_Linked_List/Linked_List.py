class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next # pointer to the next element


class LinkedList:
    def __init__(self):
        self.head = None  # points to the head of the linked list

    def insert_at_beginning(self, data):
        node = Node(data, self.head) # NEXT element will be the self.head,
                                    # which refers to the CURRENT head (which gonna be old after the update)
        self.head = node # new head is updated to be the new node
                            # think it like a snake, start of the linkedlist is always a head
                            # always treat head as a node, and it has an object of class Node,
                            # so it has data and next attribute


    def insert_at_the_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next: #when there is a next element
            itr = itr.next

        itr.next = Node(data, None) #itr.next over here refers to pointer at the last node


    def insert_values(self, data_list): # put list values in linked list (appended on blank linked list)
        self.head = None # head to be at blank linked list
        for data in data_list:
            self.insert_at_the_end(data)


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


    def get_length(self): #get length of the linked list
                            # this is good cuz can create remove element
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next

        return count


    def remove_element_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")

        if index == 0: #special case
            self.head = self.head.next # just change the head to the next element
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1: # dont be confused!
                itr.next = itr.next.next
                break
            count+=1
            itr = itr.next


    def insert_at(self, index, data):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)

        count = 0
        itr = self.head
        while itr:
            if count == index - 1: #refer to video
                node = Node(data, itr.next)
                itr.next = node
                return
            count+=1
            itr = itr.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_values([2, 5, 8, 6, 77])
    ll.remove_element_at(2)
    ll.print()
    ll.insert_at(3, "hi")

    ll.print()
    print(ll.get_length())
    pass
