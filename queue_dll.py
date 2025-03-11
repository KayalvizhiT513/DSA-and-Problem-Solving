class NodeDL:
    def __init__(self,  val):
        self.id = val
        self.next = None
        self.prev = None

class Queue:
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

    def push_range(self, range_of_val):
        for val in range_of_val:
            self.push(val)

    def print(self):
        if self.empty():
            print("Queue empty")
            return
        node = self.head
        while node:
            print(node.id)
            node = node.next

    def front(self):
        return self.head.id

    def back(self):
        return self.tail.id

    def empty(self):
        return self.head == None

    def pop(self):
        if self.empty():
            print("Queue empty")
            return
        if self.head == self.tail:
            popped_element = self.tail.id
            self.head = None
            self.tail = None
            return popped_element
        
        popped_element = self.head.id
        self.head = self.head.next
        self.head.prev = None
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
            print("Queue empty")
            return
        node = self.tail
        while node:
            print(node.id)
            node = node.prev  

def main():
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)

    print("Front element is", queue.front())
    print("Back element is", queue.back())
    print(queue.pop(), "is popped")
    print("Print queue")
    queue.print()
    print("Size of the stack:",queue.size())
    print(queue.pop(), "is popped")
    print("Reverse print queue")
    queue.reverse_print()
    print(queue.pop(), "is popped")
    print(queue.pop(), "is popped")
    queue.print()

if __name__ == "__main__":
    main()
