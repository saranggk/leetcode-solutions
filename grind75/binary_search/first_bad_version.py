"""
Problem: First Bad Version
Link: https://leetcode.com/problems/first-bad-version/
Difficulty: Easy
Time Complexity: O(log n)
Space Complexity: O(1)
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left != right:
            mid = ((left + right) // 2)
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid
        return left