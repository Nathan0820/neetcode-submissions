class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cleaned = set(nums)
        res = 0
        for num in cleaned:
            if num - 1 in cleaned:
                continue
            length = 1
            while num + length in cleaned:
                length += 1
            res = max(res, length)
        return res