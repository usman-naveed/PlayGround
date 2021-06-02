def findDuplicates(self, nums):
    hash_table = {}
    result = []

    for i in range(len(nums)):
        if nums[i] in hash_table.keys():
            hash_table[nums[i]] += 1
        else:
            hash_table[nums[i]] = 1

    for k, v in hash_table.items():
        if v > 1:
            result.append(k)
    return result
