from queue import Queue


class Queue:
    def __init__(self):
        self.stack = []

    def enqueue(self, item):
        self.stack.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.stack.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.stack[0]
        else:
            raise IndexError("peek from empty queue")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

