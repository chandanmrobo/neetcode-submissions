class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        from collections import Counter as ct
        return ct(s)==ct(t)
solution = Solution()
print(solution.isAnagram("racecar", "carrace"))  # Output: True
print(solution.isAnagram("jar", "jam"))          # Output: False
