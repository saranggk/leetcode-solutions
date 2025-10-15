"""
Problem: Invert Binary Tree
Link: https://leetcode.com/problems/invert-binary-tree/
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(h)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        dummy = root.left
        root.left = root.right
        root.right = dummy
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root