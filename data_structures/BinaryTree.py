class BTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BT:
    def __init__(self, root):
        self.root = root

    def pre_order(self, current):
        print(current.val, end="->")
        if current.left:
            self.pre_order(current.left)
        if current.right:
            self.pre_order(current.right)

    def in_order(self, current):
        if current.left is not None:
            self.in_order(current.left)
        print(current.val, end="->")
        if current.right is not None:
            self.in_order(current.right)

    def post_order(self, current):
        if current.left is not None:
            self.post_order(current.left)
        if current.right is not None:
            self.post_order(current.right)
        print(current.val, end="->")


root = BTNode(5)
root.right = BTNode(8)
root.left = BTNode(99)
root.left.left = BTNode(10000)
root.left.right = BTNode(9000)
bt = BT(root)
print("PRE-ORDER")
bt.pre_order(root)
print("")
print("IN-ORDER")
bt.in_order(root)
print("")
print("POST-ORDER")
bt.post_order(root)




