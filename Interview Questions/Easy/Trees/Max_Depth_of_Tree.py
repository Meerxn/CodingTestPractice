class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        l = None
        r = None
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        if root.left != None:
            if root.left.val < root.val:
                l = self.isValidBST(root.left)
            else:
                l =  False
        if root.right != None:
            if root.right.val > root.right:
                r =  self.isValidBST(root.right)
            else:
                r=  False    

        if l == False or r == False:
            return False