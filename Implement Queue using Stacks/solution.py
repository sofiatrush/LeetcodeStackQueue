"""Implement Queue using Stacks"""

class Stack:
    """
    Simple stack implementation using a list.
    """

    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.items = []

    def push(self, item):
        """
        Push an item onto the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Remove and return the top item from the stack.
        """
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        """
        Return the top item without removing it.
        """
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        """
        Check if the stack is empty.
        """
        return len(self.items) == 0

    def size(self):
        """
        Return the number of items in the stack.
        """
        return len(self.items)


class MyQueue:
    """
    Queue implemented using two stacks.
    """

    def __init__(self):
        """
        Initialize two stacks for the queue.
        """
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, item):
        """
        Add an item to the end of the queue.
        """
        self.stack1.push(item)

    def pop(self):
        """
        Remove and return the front item from the queue.
        """
        if self.stack2.is_empty():
            for _ in range(self.stack1.size()):
                element = self.stack1.pop()
                self.stack2.push(element)
        return self.stack2.pop()

    def peek(self):
        """
        Return the front item without removing it.
        """
        if self.stack2.is_empty():
            for _ in range(self.stack1.size()):
                element = self.stack1.pop()
                self.stack2.push(element)
        return self.stack2.peek()

    def empty(self):
        """
        Check if the queue is empty.
        """
        return self.stack1.is_empty() and self.stack2.is_empty()
