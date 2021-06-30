class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lp = 0
        rp = 0
        max_len = 0
        hash_set = {}
        if s is None:
            return 0
        else:
            while rp < len(s):
                if s[rp] not in hash_set.keys():
                    hash_set[s[rp]] = 1
                    rp += 1
                    max_len = max(len(hash_set), max_len)
                else:
                    hash_set.pop(s[lp])
                    lp += 1

        return max_len