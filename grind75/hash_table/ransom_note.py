"""
Problem: Ransom Note
Link: https://leetcode.com/problems/ransom-note/
Difficulty: Easy
Time Complexity: O(m + n)
Space Complexity: O(1)
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        table = {}
        for char in magazine:
            table[char] = table.get(char, 0) + 1
        for char in ransomNote:
            if char in table and table[char] > 0:
                table[char] -= 1
            else:
                return False
        return True