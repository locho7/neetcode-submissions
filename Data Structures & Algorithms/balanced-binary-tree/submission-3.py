# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:  
        def isBalancedHelper(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0

            left = isBalancedHelper(root.left)
            right = isBalancedHelper(root.right)

            if left == -1:
                return -1
            
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return isBalancedHelper(root) != -1
                