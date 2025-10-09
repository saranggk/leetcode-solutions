"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, j in enumerate(nums):
            diff = target - j
            if diff in seen:
                return [seen[diff], i]
            seen[j] = i