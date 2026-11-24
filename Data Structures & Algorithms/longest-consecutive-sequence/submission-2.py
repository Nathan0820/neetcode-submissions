class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1. preprocess nums into a set
        # 2. find the starting number
        # 3. track the length of the sequence
        # 4. res = max(res, length)

        set_nums = set(nums)
        res = 0
        for num in nums:
            # check if num is the first in sequence
            if num - 1 in set_nums:
                continue
            length = 1
            while num + length in set_nums:
                length += 1
            res = max(res, length)
        return res