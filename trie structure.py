import os

def clear():
    # Clears the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
class TreeNode:
    def __init__(self, val):
        self.data = val
        self.children = {}
        self.end_of_word = False

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
    
def main():
    # build tree
    root = TreeNode('*')

    vocabulary = []

    file1 = open("english-words.txt", "r")
    word = file1.readline()

    count = 0 
    while word != '':
        print(word)
        vocabulary.append(word)
        word = file1.readline()
        count += 1
        if count == 1000:
            break

    file1.close()
    
    for word in vocabulary:
        node = root
        for char in word:
            if char == '\n':
                continue
            if char not in node.children.keys():
                node.children[char] = TreeNode(char)
            node = node.children[char]
        node.end_of_word = True

    for word in vocabulary:
        node = root
        for char in word:
            if char not in node.children.keys():
                
            node = node.children[char]
        
    # Level Order traversal
    if False:
        print("Level Order traversal:")
        queue = Queue()

        queue.push(root)
        while not queue.empty():
            curr = queue.pop()
            print(curr.data, end=" ")

            for char in curr.children.values():
                queue.push(char)
    

if __name__ == "__main__":
    main()
