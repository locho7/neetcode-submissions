# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def treeHeight(tree: Optional[TreeNode]) -> int:
            if tree is None:
                return 0
            return (1 + max(treeHeight(tree.left),
                            treeHeight(tree.right)))
                
        leftHeight = treeHeight(root.left)
        rightHeight = treeHeight(root.right)

        if abs(leftHeight - rightHeight) > 1:
            return False
        
        return (self.isBalanced(root.left) and 
                self.isBalanced(root.right))