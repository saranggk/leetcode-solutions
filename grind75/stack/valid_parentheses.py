"""
Problem: Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_brackets = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            if char == ')' or char == ']' or char == '}':
                if stack and (stack[-1] == matching_brackets[char]):
                    stack.pop()
                else:
                    return False
        return not stack