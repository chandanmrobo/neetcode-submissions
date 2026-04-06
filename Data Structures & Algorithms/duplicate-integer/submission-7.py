class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=set()
        for i in nums:
            if i in a:
                return True
            a.add(i)
        return False
nums1 = [1, 2, 3, 3]
nums2 = [1, 2, 3, 4]

solution = Solution()
print(solution.hasDuplicate(nums1))
print(solution.hasDuplicate(nums2))

