# Template of a node in our linked list
class Node:
    def __init__(self):
        self.id = -1
        self.next = None

def main():
    # Generate 1000 lines of data
    data = [str(num).zfill(4) for num in range(1, 1001)]
    print("First 100 elements is data:", data[:100])

    # Create buffer as circular linked list
    head = Node() 
    node = head
    for i in range(1, 100):
        node.next = Node()
        node = node.next
    node.next = head

    # Storing data
    node = head
    for ele in data:
        node.id = ele
        node = node.next

    # Print the elements in buffer
    print("Data in buffer:")
    node = head.next
    print(head.id, end=' ')
    while id(node) != id(head):
        print(node.id, end=' ')
        node = node.next
        
if __name__ == '__main__':
    main()



