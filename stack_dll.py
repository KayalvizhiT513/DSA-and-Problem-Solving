class NodeDL:
    def __init__(self,  val):
        self.id = val
        self.next = None
        self.prev = None

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val):
        if self.empty():
            self.head = NodeDL(val)
            self.tail = self.head
        else:
            self.tail.next = NodeDL(val)
            old_tail = self.tail
            self.tail = self.tail.next
            self.tail.prev = old_tail

    def print(self):
        if self.empty():
            print("Stack empty")
            return
        node = self.head
        while node:
            print(node.id)
            node = node.next

    def top(self):
        return self.tail.id

    def empty(self):
        return self.head == None

    def pop(self):
        if self.empty():
            print("Stack empty")
            return
        if self.head == self.tail:
            popped_element = self.tail.id
            self.head = None
            self.tail = None
            return popped_element
        popped_element = self.tail.id
        self.tail = self.tail.prev
        self.tail.next = None
        return popped_element

    def size(self):
        count = 0
        node = self.head
        while node:
            node = node.next
            count += 1
        return count

    def reverse_print(self):
        if self.empty():
            print("Stack empty")
            return
        node = self.tail
        while node:
            print(node.id)
            node = node.prev        

def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print("Top element is", stack.top())
    print(stack.pop(), "is popped")
    print("Print stack")
    stack.print()
    print("Size of the stack:",stack.size())
    print(stack.pop(), "is popped")
    print("Reverse print stack")
    stack.reverse_print()
    print(stack.pop(), "is popped")
    print(stack.pop(), "is popped")
    stack.print()

if __name__ == "__main__":
    main()
