"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        '''add new element to the tail'''
        self.storage.append(new_element)

    def peek(self):
        '''look at the head'''
        return self.storage[0]

    def dequeue(self):
        '''pop the head'''
        buffer = self.storage.pop(0)
        return buffer

# Test cases
if __name__ == '__main__':
    # Setup
    q = Queue(1)
    q.enqueue(2)
    q.enqueue(3)

    # Test peek
    print(q.peek())                     # 1

    # Test dequeue
    print(q.dequeue())                  # 1

    # Test enqueue
    q.enqueue(4)                        # 2
    print(q.dequeue())                  # 3
    print(q.dequeue())                  # 4
    print(q.dequeue())
    q.enqueue(5)
    print(q.peek())                     # 5
