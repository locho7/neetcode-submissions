# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0

        def heightOfBinaryTree(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            
            left = heightOfBinaryTree(root.left)
            right = heightOfBinaryTree(root.right)
            self.maxDiameter = max(self.maxDiameter, left + right)

            return (1 + max(left,right))

        heightOfBinaryTree(root)

        return self.maxDiameter
