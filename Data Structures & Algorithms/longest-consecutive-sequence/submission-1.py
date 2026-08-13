class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = set(nums)
        res = 0
        for num in dic:
            if num - 1 in dic:
                continue
            length = 1
            while num + length in dic:
                length += 1
            res = max(res, length)
        return res