"""
Problem: Flood Fill
Link: https://leetcode.com/problems/flood-fill/
Difficulty: Easy
Time Complexity: O(m x n)
Space Complexity: O(m x n)
"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        self.fill(image, sr, sc, image[sr][sc], color)
        return image

    def fill(self, image, sr, sc, old_color, color):
        if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != old_color:
            return
        image[sr][sc] = color
        self.fill(image, sr-1, sc, old_color, color)
        self.fill(image, sr+1, sc, old_color, color)
        self.fill(image, sr, sc-1, old_color, color)
        self.fill(image, sr, sc+1, old_color, color)