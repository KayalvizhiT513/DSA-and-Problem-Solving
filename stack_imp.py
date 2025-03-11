class Node:
    def __init__(self):
        self.id = -1
        self.next = None

class NodeDL:
    def __init__(self):
        self.id = -1
        self.next = None
        self.prev = None

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    def print(self):
        node = slef.head
        while node:
            print(node.id)
            node = node.next

    def top(self):
        return self.tail.id


def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print("Top element is", stack.top())
