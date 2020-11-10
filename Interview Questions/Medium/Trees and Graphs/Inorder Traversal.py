# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorderTraversal(root):
    #leaf node
    if root == None:
        return None
    elif root.left == None and root.right == None:
        return [root.val]
    else:

        
        lval = inorderTraversal(root.left)

        rval = inorderTraversal(root.right)

        if lval == None and rval != None:
            rval.insert(0,root.val)
            return rval
        elif lval != None and rval == None: 
            lval.append(root.val)
            return lval
        else:
            lval.append(root.val)
            lval = lval + rval
            return lval


