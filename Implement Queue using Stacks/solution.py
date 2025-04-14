class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

class MyQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
    def push(self, item):
        self.stack1.push(item)
    def pop(self):
        if self.stack2.is_empty():
            for _ in range(self.stack1.size()):
                element = self.stack1.pop()
                self.stack2.push(element)
        return self.stack2.pop()
    def peek(self):
        if self.stack2.is_empty():
            for _ in range(self.stack1.size()):
                element = self.stack1.pop()
                self.stack2.push(element)
        return self.stack2.peek()
    def empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()

