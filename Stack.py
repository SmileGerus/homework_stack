class Stack:
    def __init__(self, stack: list):
        self.stack = stack

    def is_empty(self):
        if not self.stack:
            return True
        return False

    def pop(self):
        if not self.stack:
            return None
        removed: int = self.stack.pop()
        return removed

    def push(self, item: int):
        self.stack.append(item)

    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)
