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

class FreqStack:
    def __init__(self):
        self.number_to_count = {}
        self.count_to_stack = {}
        self.current_max_count = 0

    def push(self, number: int) -> None:
        if number in self.number_to_count:
            self.number_to_count[number] += 1
        else:
            self.number_to_count[number] = 1

        count = self.number_to_count[number]

        if count > self.current_max_count:
            self.current_max_count = count

        if count not in self.count_to_stack:
            self.count_to_stack[count] = Stack()

        self.count_to_stack[count].push(number)

    def pop(self) -> int:
        max_stack = self.count_to_stack[self.current_max_count]
        number = max_stack.pop()
        self.number_to_count[number] -= 1

        if max_stack.is_empty():
            self.current_max_count -= 1

        return number
