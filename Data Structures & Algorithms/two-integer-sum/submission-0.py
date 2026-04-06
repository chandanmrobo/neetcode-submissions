class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s={}
        for i,value in enumerate(nums):
            c=target-value
            if c in s:
                return [s[c],i]
            s[value]=i