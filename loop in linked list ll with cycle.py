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

    node4 = StudentNode()
    node4.student_id = 4
    node4.age = 31
    node3.next_link = node4

    node5 = StudentNode()
    node5.student_id = 5
    node5.age = 24
    node4.next_link = node5
    node5.next_link = node4


    def loop_in_list_On():
        current = node1
        nodeid_list = []
        while current:
            if not id(current) in nodeid_list:
                nodeid_list.append(id(current))
                current = current.next_link
            else:
                return True
        return False

    
    print("Loop in the linked list O(n):", loop_in_list_On())

    def loop_in_list_O1():
        current1 = node1
        current2 = node2
        
        while current1 and current2:
            if id(current1) != id(current2):
                current1 = current1.next_link
                current2 = current2.next_link.next_link
            else:
                return True
        return False

    
    print("Loop in the linked list O(1):", loop_in_list_O1())
    
if __name__ == '__main__':
    main()
