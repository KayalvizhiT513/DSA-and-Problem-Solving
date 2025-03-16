class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
def main():
    L1 = [1,2,3,4,5]
    L2 = [1,2,3,4]
    print("Defined lists:")
    print(f"L1: {L1}")
    print(f"L2: {L2}")

    head1 = Node(L1[0])
    node = head1
    for i in range(1, len(L1)):
        node.next = Node(L1[i])
        node.next.prev = node
        node = node.next
    tail1 = node

    head2 = Node(L2[0])
    node = head2
    for i in range(1, len(L2)):
        node.next = Node(L2[i])
        node.next.prev = node
        node = node.next
    node.next = head1.next.next.next
    tail2 = node

    def print_list(node):
        while node:
            print(node.val, end=' ')
            node = node.next

    print("Initial linked lists:")
    print("L1: ",end='')
    print_list(head1)
    print()
    print("L2: ",end='')
    print_list(head2)

    node2 = head2
    last_node = None
    while node2:
        node1 = head1
        while node1 and id(node1) != id(node2):
            node1 = node1.next
        if id(node1) == id(node2):
            last_node.next = None
            break
        last_node = node2
        node2 = node2.next
        
    print("\nAfter fixing L2 last_node:")
    print("L1: ",end='')
    print_list(head1)
    print()
    print("L2: ",end='')
    print_list(head2)
    
if __name__ == '__main__':
    main()
    

         
