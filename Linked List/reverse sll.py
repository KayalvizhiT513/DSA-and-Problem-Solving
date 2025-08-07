class Node:
    def __init__(self, val):
        self.id = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val):
        if self.empty():
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    def print(self):
        if self.empty():
            print("Stack empty")
            return
        node = self.head
        while node:
            print(node.id)
            node = node.next

    def top(self):
        return self.tail.id if self.tail else None

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
        node = self.head
        while node.next.next:
            node = node.next
        popped_element = node.next.id
        self.tail = node
        self.tail.next = None
        return popped_element

    
def main():
    name1 = 'Ilamathi'
    
    name1_head = Node(name1[0])
    node = name1_head
    for char in name1[1:]:
        node.next = Node(char)
        node = node.next

    def print_list():
        current = name1_head
        while current:
            print(current.id, end='')
            current = current.next
        print()

    def reverse_list_with_recursion(node, head):
        if node.next == None:
            head = node
            return node, head
        prev, head = reverse_list_with_recursion(node.next, head)
        prev.next = node
        node.next = None
        return node, head

    def reverse_list_with_stack(name1_head):
        stack = Stack()
        node = name1_head
        while node:
            stack.push(node)
            node = node.next

        name1_head = stack.pop()
        node = name1_head
        while stack.top():
            node.next = stack.pop()
            node = node.next
        node.next = None

        return name1_head

    print("Data in original linked list:")
    print_list()

    print("Reversed using Stack:")
    name1_head = reverse_list_with_stack(name1_head)
    print_list()

    print("Reversed using Recursion:")
    tail, name1_head = reverse_list_with_recursion(name1_head, name1_head)
    print_list()

if __name__ == '__main__':
    main()
