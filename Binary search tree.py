class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

    def push(self, val):
        if val < self.data:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.push(val)
        elif val > self.data:
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.push(val)
    
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data, end=' ')
        if self.right:
            self.right.inorder()

    def preorder(self):
        print(self.data, end=' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data, end=' ')

def main():
    # build tree
    root = TreeNode(4)
    root.push(2)
    root.push(6)
    root.push(1)
    root.push(3)
    root.push(5)
    root.push(7)

    print("Inorder traversal:")
    root.inorder()
    print("\nPreorder traversal:")
    root.preorder()
    print("\nPostorder traversal:")
    root.postorder()
    

if __name__ == "__main__":
    main()
