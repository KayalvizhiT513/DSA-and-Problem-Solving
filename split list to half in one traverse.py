class NodeDL:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def split_list(head, tail):
    node1 = head
    node2 = tail

    while id(node1) != id(node2) and id(node1.next) != id(node2):
        node1 = node1.next
        node2 = node2.prev
    if id(node1) == id(node2):
        node1.prev.next = None
        node2.prev = None
    else:
        node1.next = None
        node2.prev = None

    return head, node2
    
def main():
    L1 = [1,2,3,4,5]
    L2 = [1,2,3,4]

    head1 = NodeDL(L1[0])
    node = head1
    for i in range(1, len(L1)):
        node.next = NodeDL(L1[i])
        node.next.prev = node
        node = node.next
    tail1 = node

    head2 = NodeDL(L2[0])
    node = head2
    for i in range(1, len(L2)):
        node.next = NodeDL(L2[i])
        node.next.prev = node
        node = node.next
    tail2 = node

    # Splitting L1
    head1_1, head1_2 = split_list(head1, tail1)

    # Splitting L2
    head2_1, head2_2 = split_list(head2, tail2)

    def print_list(node):
        while node:
            print(node.val, end=' ')
            node = node.next

    print(f"L1 first half:")
    print_list(head1_1)
    print(f"\nL1 second half:")
    print_list(head1_2)
    print()
    print(f"L2 first half:")
    print_list(head2_1)
    print(f"\nL2 second half:")
    print_list(head2_2)
    
if __name__ == '__main__':
    main()
    

         
