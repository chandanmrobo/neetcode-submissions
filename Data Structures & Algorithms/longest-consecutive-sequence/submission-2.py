class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        a = set(nums)
        long = 0
        for num in a:
            if num - 1 not in a:
                l = 1
                while num + l in a:
                    l += 1
                long = max(long, l)
        return long