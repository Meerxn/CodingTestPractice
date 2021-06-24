# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root == None:
            return result
        queue = []
        queue.append(root)
        while (len(queue) > 0 ):
            currLevel = []
            for i in range(len(queue)):
                curr = queue.pop(0)
                currLevel.append(curr.val)
                if(curr.left):
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(currLevel)
        return result
                
        