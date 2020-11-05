# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root.left.val == 0 and root.right == 0  :
            return True

        val = (self.isValidBST(root.left),self.isValidBST(root.right))    
        if root.left.val >= root.val or root.right.val < root.val or False in val:
            return False
        else:
             return True        

        