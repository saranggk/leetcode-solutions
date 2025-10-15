"""
Problem: Valid Palindrome
Link: https://leetcode.com/problems/valid-palindrome/
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not self.checkAlphaNum(s[left]):
                left += 1
            while right > left and not self.checkAlphaNum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def checkAlphaNum(self, char):
        return (ord('0') <= ord(char) <= ord('9') or
                ord('a') <= ord(char) <= ord('z') or
                ord('A') <= ord(char) <= ord('Z'))