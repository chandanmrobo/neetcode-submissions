class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = set(nums)
        long=0
        for num in nums:
            if num -1 not in a:
                l=1
                while num+l in a:
                    l+=1
                long=max(long,l)
        return long