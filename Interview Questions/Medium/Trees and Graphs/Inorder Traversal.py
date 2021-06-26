class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        self.helper(root,ans)
        return ans
    
    def helper(self,root,res):
        if root != None:
            self.helper(root.left,res)
            res.append(root.val)
            self.helper(root.right,res)
        else:
            return
            
            