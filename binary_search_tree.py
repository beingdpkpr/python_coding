
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def Insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.Insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.Insert(value)
        else:
            self.value = value

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.value)
        if self.right:
            self.right.PrintTree()

    def Inorder(self, root):
        res = []
        if root:
            res = self.Inorder(root.left)
            res.append(root.value)
            res = res + self.Inorder(root.right)
        return res

    def Postorder(self, root):
        res = []
        if root:
            res = self.Postorder(root.right)
            res.append(root.value)
            res = res + self.Postorder(root.left)
        return res


root = Node(27)
root.Insert(14)
root.Insert(35)
root.Insert(10)
root.Insert(19)
root.Insert(31)
root.Insert(42)
print(root.Inorder(root))
print(root.Postorder(root))
