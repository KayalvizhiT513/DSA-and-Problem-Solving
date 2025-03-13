class NodeDL:
    def __init__(self,  val):
        self.id = val
        self.next = None
        self.prev = None

    def print(head):
        node = head
        while node:
            print(node.id, end=" ")
            node = node.next
        print()

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
    name1 = 'Ilamathi'
    
    name1_head = NodeDL(name1[0])
    node = name1_head
    for char in name1[1:]:
        prev_node = node
        node.next = NodeDL(char)
        node = node.next
        node.prev = prev_node

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
       
        node = stack.pop()
        node.prev = None
        name1_head = node
        while stack.top():
            prev_node = node
            node.next = stack.pop()
            node = node.next
            node.prev = prev_node
        node.next = None

        return name1_head

    print("Data in original linked list:")
    name1_head.print()

    print("Reversed using Stack:")
    name1_head = reverse_list_with_stack(name1_head)
    name1_head.print()

if __name__ == '__main__':
    main()
