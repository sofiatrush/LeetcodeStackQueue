"""Maximum Frequency Stack"""

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


class FreqStack:
    """
    Stack that supports push and pop based on frequency.
    """

    def __init__(self):
        """
        Initialize data structures to track frequencies and stacks.
        """
        self.number_to_count = {}
        self.count_to_stack = {}
        self.current_max_count = 0

    def push(self, number: int) -> None:
        """
        Push a number onto the frequency stack.
        """
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
        """
        Remove and return the most frequent element.
        """
        max_stack = self.count_to_stack[self.current_max_count]
        number = max_stack.pop()
        self.number_to_count[number] -= 1

        if max_stack.is_empty():
            self.current_max_count -= 1

        return number
