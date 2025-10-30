"""
Problem: Longest Palindrome
Link: https://leetcode.com/problems/longest-palindrome/
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = defaultdict(int)
        count = 0
        for char in s:
            freq[char] += 1
            if freq[char] % 2 == 0:
                count += 2
        if any(val % 2 for val in freq.values()):
            count += 1
        return count
