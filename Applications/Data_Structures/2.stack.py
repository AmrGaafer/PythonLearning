"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None                # type is Element


class LinkedList(object):
    def __init__(self, head=None):      # head should be Element type
        self.head = head                # first element is head
    
    def append(self, new_element):      # O(n)
        '''appending elements after head element'''
        current = self.head
        if self.head:                   # only if linked list has elements
            while current.next:
                current = current.next
            current.next = new_element
        else:                           # if linked list inisialized without elements 
            self.head = new_element
    
    def insert_first(self, new_element):
        '''Insert new element as the head of the LinkedList'''
        if self.head:                   # only if linked list has elements
            new_element.next = self.head
            self.head = new_element
        else:
            self.head = new_element
    
    def delete_first(self):
        '''Delete the first (head) element in the LinkedList as return it'''
        buffer = self.head
        if self.head:                   # only if linked list has elements
            self.head = self.head.next
            buffer.next = None
        return buffer


class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)
    
    def push(self, new_element):
        '''Push (add) a new element onto the top of the stack'''
        self.ll.insert_first(new_element)
    
    def pop(self):
        '''Pop (remove) the first element off the top of the stack and return it'''
        return self.ll.delete_first()


# Test cases
if __name__ == '__main__':
    # Set up some Elements
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    # Start setting up a Stack
    stack = Stack(e1)

    # Test stack functionality
    stack.push(e2)
    stack.push(e3)
    print(stack.pop().value)
    print(stack.pop().value)
    print(stack.pop().value)
    print(stack.pop())
    stack.push(e4)
    print(stack.pop().value)
