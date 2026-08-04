# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        invertTreeHelper(root)
        return root

def invertTreeHelper(tree):
    if tree is None:
        return

    left = tree.left
    right = tree.right

    tree.right = left
    tree.left = right

    invertTreeHelper(left)
    invertTreeHelper(right)
    