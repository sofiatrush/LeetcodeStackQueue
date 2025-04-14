class Queue:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)

    def peek(self):
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def length(self):
        return len(self.items)

class MyStack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, item):
        self.queue2.add(item)
        for _ in range(self.queue1.length()):
            element = self.queue1.pop()
            self.queue2.add(element)
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        return self.queue1.pop()

    def top(self) -> int:
        return self.queue1.peek()

    def empty(self) -> bool:
        return self.queue1.is_empty()
