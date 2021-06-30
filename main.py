
# class Solution:
#     def in_order(self, tree, result=None):
#         if result is None:
#             result = []
#         if tree.left:
#             self.in_order(tree.left, result)
#         result.append(tree.val)
#         if tree.right:
#             self.in_order(tree.right, result)
#         return result
#
#     def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#         # traverse each tree and store each node value in a result array
#         # then compare the result arrays to see if the trees are equal. If trees are equal, then
#         # the resulting arrays will be equal
#         if p == q:
#             return True
#         if p is not None and q is None:
#             return False
#         if q is not None and p is None:
#             return False
#         result_p = self.in_order(p)
#         result_q = self.in_order(q)
#         return result_p == result_q