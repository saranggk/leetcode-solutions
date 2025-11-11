"""
Problem: Majority Element
Link: https://leetcode.com/problems/majority-element/
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = 0, 0
        for i in nums:
            if count == 0:
                candidate = i
                count = 1
            elif candidate == i:
                count += 1
            else:
                count -= 1
        return candidate
