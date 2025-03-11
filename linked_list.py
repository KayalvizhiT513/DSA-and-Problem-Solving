# Template of a node in our linked list
class StudentNode:
    def __init__(self):
        self.student_id = -1
        self.age = -1
        self.next_link = None

def main():
    node1 = StudentNode() # from here we have a data in memory
    node1.student_id = 1
    node1.age = 20

    node2 = StudentNode()
    node2.student_id = 2
    node2.age = 21

    # Two nodes are created seperatedly in memory
    # Next creating link
    node1.next_link = node2

    node3 = StudentNode()
    node3.student_id = 3
    node3.age = 21
    node2.next_link = node3

    def text_funct():
        print("Hello, text message here")
        
    print("Address of nodes in stack:")
    print(f"{id(node1)} -> {id(node1.next_link)}")
    print(f"{id(node2)} -> {id(node2.next_link)}")
    print(f"{id(node3)} -> {id(node3.next_link)}")

    print("Address of text in heap:")
    print(f"{id(text_funct)}")

    def print_list(node):
        current = node
        while current:
            print(current.student_id, end=" ")
            current = current.next_link

    def reverse_print_list(node):
        if node is None:
            return
        reverse_print_list(node.next_link)
        print(node.student_id, end=" ")

    print_list(node1)
    print()
    reverse_print_list(node1)
    
if __name__ == '__main__':
    main()
