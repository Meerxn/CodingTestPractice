# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        if root is None: 
            return
# Create an empty queue for level order traversal 
        q = [] 
        dict = {}
        imd = {}

# Enqueue root and initialize height 
        q.append(root)
        kFound = False 
        level = 0
        kLevel =  0  
        while q: 

# nodeCount (queue size) indicates number 
# of nodes at current lelvel. 
            count = len(q)
             

            # Dequeue all nodes of current level and 
            # Enqueue all nodes of next level 
            while count > 0: 
                temp = q.pop(0)
                if temp.val == k:
                    kFound == True
                    kLevel = level
                    imd["left"] = temp.left.val
                    imd["right"] = temp.right.val
                if not temp.left and not temp.right and temp.val in imd.values():
                    dict[temp.val] = level - 1
                elif not temp.left and not temp.right and  temp.val not in imd.values() :
                    dict[temp.val] = level  
                if temp.left or temp.right:
                    level = level + 1
                if temp.left: 
                    q.append(temp.left) 
                if temp.right: 
                    q.append(temp.right)
                
            
                count -= 1
        print(dict.items())    
        for k in dict:
            
            dict[k]  = abs(dict[k] - kLevel)
        print(dict.items())
        print(kLevel)
        return min(dict,key=dict.get)    