# Template of a node in our linked list
class Node:
    def __init__(self):
        self.id = -1
        self.next = None

def main():
    name1 = 'Ilamathi' # m
    name2 = 'Ilavazhuthi' #vzuh

    name1_head = Node()
    name1_head.id = name1[0]
    node = name1_head
    for char in name1[1:]:
        node.next = Node()
        node = node.next
        node.id = char

    name2_head = Node()
    name2_head.id = name2[0]
    node = name2_head
    for char in name2[1:]:
        node.next = Node()
        node = node.next
        node.id = char

    # Remove matched chars from the names
    curr1 = name1_head
    curr2 = name2_head
    prev1 = None
    prev2 = None
    while curr1:
        curr2 = name2_head
        prev2 = None
        while curr2:
            if curr1.id == curr2.id:
                if prev1:
                    prev1.next = curr1.next
                    curr1 = curr1.next
                else:
                    name1_head = curr1.next
                    curr1 = curr1.next
                if prev2:
                    prev2.next = curr2.next
                else:
                    name2_head = curr2.next
                break
            elif curr2.next:
                prev2 = curr2
                curr2 = curr2.next
            else:
                prev1 = curr1
                curr1 = curr1.next
                break                        

    # Print the elements in buffer
    print("After removing common characters:")
    node = name1_head
    while node:
        print(node.id, end='')
        node = node.next

    print()
    node = name2_head
    while node:
        print(node.id, end='')
        node = node.next

    # Count remaing number of chars
    count = 0
    node = name1_head
    while node:
        count += 1
        node = node.next

    node = name2_head
    while node:
        count += 1
        node = node.next

    # Implement Flames circular linked list
    head = Node()
    head.id = 'F'
    node = head
    for char in 'LAMES':
        node.next = Node()
        node = node.next
        node.id = char
    node.next = head

    prev = node
    node = head
    while id(node) != id(node.next):
        for i in range(count-1):
            prev = node
            node = node.next
        prev.next = node.next
        node = node.next

    print(f"\n{name1} & {name2} will be",node.id)
            
if __name__ == '__main__':
    main()
