"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None                # type is Element


class LinkedList(object):
    def __init__(self, head=None):      # head should be Element type
        self.head = head                # first element is head
    
    def append(self, new_element):      # O(n)
        current = self.head
        if self.head:                   # only if linked list has elements
            while current.next:
                current = current.next
            current.next = new_element
        else:                           # if linked list inisialized without elements 
            self.head = new_element
    
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        if self.head:                               # only if linked list has elements
            for i in range(1, position):
                if current.next:
                    current = current.next
                else:
                    return None
        return current
    
    def insert(self, new_element, position):        # O(n)
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current = self.head
        if self.head:                               # only if linked list has elements
            for i in range(1, position-1):
                if current.next:
                    current = current.next
                else:
                    pass
            else:
                new_element.next = current.next     # firstly map pointer of new_element to next element
                current.next = new_element          # secondly map pointer of current to new_element
    
    def delete(self, value):                        # O(n)
        """Delete the first node with a given value."""
        current = self.head
        if self.head:                               # only if linked list has elements
            if self.head.value == value:            # check if the head neads to be removed
                self.head = current.next
                return None
            while current:                          # check if any successive element to be removed
                if current.next.value == value:
                    current.next = current.next.next
                current = current.next


# Test cases
if __name__ == '__main__':
    # Set up some Elements
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)
    e5 = Element(5)
    e6 = Element(6)
    e7 = Element(7)
    e8 = Element(8)
    e9 = Element(9)
    e10 = Element(10)

    # Start setting up a LinkedList
    ll = LinkedList()
    ll.append(e1)
    ll.append(e2)
    ll.append(e3)
    ll.append(e5)
    ll.append(e6)
    ll.append(e7)

    # Test get_position
    print('Test get_position():')
    print(ll.head.value)                # 1
    print(ll.get_position(1).value)     # also 1
    print(ll.get_position(2).value)     # 2
    print(ll.head.next.next.value)      # 3
    print(ll.get_position(3).value)     # also 3
    print(ll.get_position(4).value)     # 5
    print(ll.get_position(5).value)     # 6
    print(ll.get_position(6).value)     # 7

    # Test insert
    print('Test insert():')
    ll.insert(e4,3)
    print(ll.head.value)                # 1
    print(ll.head.next.value)           # 2
    print(ll.head.next.next.value)      # 4 now
    print(ll.head.next.next.next.value) # 3 now
    print(ll.get_position(5).value)     # 5
    ll.insert(e10,8)
    ll.insert(e8,8)
    ll.insert(e9,9)
    print(ll.get_position(6).value)     # 6
    print(ll.get_position(7).value)     # 7
    print(ll.get_position(8).value)     # 8
    print(ll.get_position(9).value)     # 9
    print(ll.get_position(10).value)    # 10

    # Test delete
    print('Test delete():')
    ll.delete(1)
    ll.delete(10)
    print(ll.get_position(1).value)     # 2 now
    print(ll.get_position(2).value)     # 4 now
    print(ll.get_position(3).value)     # 3 now
    print(ll.get_position(8).value)     # 9 now
