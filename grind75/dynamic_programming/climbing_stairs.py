"""
Problem: Climbing Stairs
Link: https://leetcode.com/problems/climbing-stairs/
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1
        for i in range(n - 1):
            temp = one
            one += two
            two = temp
        return one