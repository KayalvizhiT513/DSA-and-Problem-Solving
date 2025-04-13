import random
import time

class Node:
    def __init__(self, data):
        self.data = data
        self.color = "RED"
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(0)
        self.NIL.color = "BLACK"
        self.NIL.left = self.NIL
        self.NIL.right = self.NIL
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def fix_insert(self, k):
        while k != self.root and k.parent.color == "RED":
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == "RED":
                    k.parent.color = "BLACK"
                    u.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == "RED":
                    k.parent.color = "BLACK"
                    u.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.left_rotate(k.parent.parent)
        self.root.color = "BLACK"

    def insert(self, data, balance=True):
        new_node = Node(data)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        if not balance:
            return

        if new_node.parent is None:
            new_node.color = "BLACK"
            return

        if new_node.parent.parent is None:
            return

        self.fix_insert(new_node)

    def search(self, data):
        return self.search_helper(self.root, data)

    def search_helper(self, node, data):
        if node == self.NIL or data == node.data:
            return node
        if data < node.data:
            return self.search_helper(node.left, data)
        return self.search_helper(node.right, data)

def main():
    rbt_no_balance = RedBlackTree()
    rbt_balance = RedBlackTree()

    # Generate 1000 unique random numbers
    numbers = random.sample(range(1, 10000000), 1000000)

    # Insert without balancing
    start_time = time.perf_counter()
    for number in numbers:
        rbt_no_balance.insert(number, balance=False)
    end_time = time.perf_counter()
    insert_time_no_balance = end_time - start_time
    print(f"Insertion time without balancing: {insert_time_no_balance:.6f} seconds")

    # Insert with balancing
    start_time = time.perf_counter()
    for number in numbers:
        rbt_balance.insert(number, balance=True)
    end_time = time.perf_counter()
    insert_time_balance = end_time - start_time
    print(f"Insertion time with balancing: {insert_time_balance:.6f} seconds")

    # Search for multiple numbers to amplify time difference
    num_searches = 10000  
    search_keys = random.sample(numbers, num_searches)

    # Search without balancing
    start_time = time.perf_counter()
    for key in search_keys:
        search_result_no_balance = rbt_no_balance.search(key)
    end_time = time.perf_counter()
    search_time_no_balance = end_time - start_time
    print(f"Search time without balancing ({num_searches} searches): {search_time_no_balance:.6f} seconds")

    # Search with balancing
    start_time = time.perf_counter()
    for key in search_keys:
        search_result_balance = rbt_balance.search(key)
    end_time = time.perf_counter()
    search_time_balance = end_time - start_time
    print(f"Search time with balancing ({num_searches} searches): {search_time_balance:.6f} seconds")

if __name__ == "__main__":
    main()