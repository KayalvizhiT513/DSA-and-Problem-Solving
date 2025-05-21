class TreeNode:
    def __init__(self, val):
        self.data = val
        self.children = None

class Node:
    def __init__(self, val):
        self.id = val
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val):
        if not val is None:
            if self.empty():
                self.head = Node(val)
                self.tail = self.head
            else:
                self.tail.next = Node(val)
                self.tail = self.tail.next

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
        return popped_element

    def size(self):
        count = 0
        node = self.head
        while node:
            node = node.next
            count += 1
        return count
    
def main():
    # build tree
    root = TreeNode('a')
    c1 = TreeNode('b')
    c2 = TreeNode('c')
    c3 = TreeNode('d')
    root.children = Node(c1)
    root.children.next = Node(c2)
    root.children.next.next = Node(c3)
    
    c11 = TreeNode('aa')
    c12 = TreeNode('ab')
    c13 = TreeNode('ac')
    c1.children = Node(c11)
    c1.children.next = Node(c12)
    c1.children.next.next = Node(c13)
    
    c21 = TreeNode('ba')
    c22 = TreeNode('bb')
    c2.children = Node(c21)
    c2.children.next = Node(c22)
    
    c211 = TreeNode('baa')
    c212 = TreeNode('bab')
    c213 = TreeNode('bac')
    c21.children = Node(c211)
    c21.children.next = Node(c212)
    c21.children.next.next = Node(c213)

    # Level Order traversal
    print("Level Order traversal:")
    queue = Queue()

    queue.push(root)
    while not queue.empty():
        curr = queue.pop()
        print(curr.data, end=" ")

        child_head = curr.children
        while child_head:
            queue.push(child_head.id)
            child_head = child_head.next
    

if __name__ == "__main__":
    main()
