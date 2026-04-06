class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        a=[1]*n
        pre=1
        for i in range(0,n):
            a[i] = pre
            pre *= nums[i]
        sur=1
        for j in range(n-1,-1,-1):
            a[j] *= sur
            sur *= nums[j]
        return a