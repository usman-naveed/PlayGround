# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def in_order(self, tree, result=None):
        if result is None:
            result = []
        if tree.left:
            self.in_order(tree.left, result)
        result.append(tree.val)
        if tree.right:
            self.in_order(tree.right, result)
        return result

    def same_structure(self, a, b):
        if a is None and b is None:
            return True
        if a is not None and b is not None:
            return self.same_structure(a.left, b.left) and self.same_structure(a.right, b.right)
        return False

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # traverse each tree and store each node value in a result array
        # then compare the result arrays to see if the trees are equal. If trees are equal, then
        # the resulting arrays will be equal. Need to also check structure with same_structure()
        if p == q:
            return True
        if p is not None and q is None:
            return False
        if q is not None and p is None:
            return False
        result_p = self.in_order(p)
        result_q = self.in_order(q)
        same_struc = self.same_structure(p, q)
        return (result_p == result_q and same_struc)

