"""Implement Stack using Queues"""

class Queue:
    """
    Simple queue implementation using a list.
    """

    def __init__(self):
        """
        Initialize an empty queue.
        """
        self.items = []

    def add(self, item):
        """
        Add an item to the end of the queue.
        """
        self.items.append(item)

    def pop(self):
        """
        Remove and return the front item from the queue.
        """
        if not self.is_empty():
            return self.items.pop(0)

    def peek(self):
        """
        Return the front item without removing it.
        """
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        """
        Check if the queue is empty.
        """
        return len(self.items) == 0

    def length(self):
        """
        Return the number of items in the queue.
        """
        return len(self.items)

class MyStack:
    """
    Stack implemented using two queues.
    """

    def __init__(self):
        """
        Initialize two queues for the stack.
        """
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, item):
        """
        Push an item onto the stack.
        """
        self.queue2.add(item)
        for _ in range(self.queue1.length()):
            element = self.queue1.pop()
            self.queue2.add(element)
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        """
        Remove and return the top item from the stack.
        """
        return self.queue1.pop()

    def top(self) -> int:
        """
        Return the top item without removing it.
        """
        return self.queue1.peek()

    def empty(self) -> bool:
        """
        Check if the stack is empty.
        """
        return self.queue1.is_empty()
