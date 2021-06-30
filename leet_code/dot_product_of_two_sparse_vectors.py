class SparseVector:
    def __init__(self, nums):
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        pointer = 0
        result = []
        while pointer < len(vec.nums):
            dot = self.nums[pointer] * vec.nums[pointer]
            result.append(dot)
            pointer += 1
        return sum(result)


# class SparseVector:
#     def __init__(self, nums: List[int]):
#         self.nums = nums
#
#     # Return the dotProduct of two sparse vectors
#     def dotProduct(self, vec: 'SparseVector') -> int:
#         pointer = 0
#         vec1 = dict()
#         vec2 = dict()
#         result = []
#         while pointer < len(vec.nums):
#             if self.nums[pointer] != 0:
#                 vec1[pointer] = self.nums[pointer]
#             if vec.nums[pointer] != 0:
#                 vec2[pointer] = vec.nums[pointer]
#             pointer += 1
#         set1 = set(vec1)
#         set2 = set(vec2)
#         common_indices = list(set1.intersection(set2))
#         for i in common_indices:
#             dot = vec1[i] * vec2[i]
#             result.append(dot)
#         return sum(result)