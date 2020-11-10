class Solution:
    #NOT DONE YET -- NEEDS FIXING
    
    def zigzagLevelOrder(root):
        direction = 'right'
        level = 1
        queue = [] 
        ans = []
        dict = {}
        ans.append([root])
        currLevel = 1
        queue.append(root)
        dict[level] = queue[0].val

        while len(queue) > 0:
            node = queue.pop(0)
           


            if direction == "left":
                ks = [] 
                if node.left != None:
                    queue.append(node.left)
                    ks.append(node.left.val)
                if node.right != None:
                    queue.append(node.right)
                    ks.append(node.right.val)
                if len(ks) > 0    
                ans.append(ks)    
            elif direction == "right":
                ks = [] 
                if node.right != None:
                    queue.append(node.right)
                    ks.append(node.right.val)
                if node.left != None:
                    queue.append(node.left)
                    ks.append(node.left.val)
                ans.append(ks) 
            if direction == "left":
                direction = "right"
            else:
                direction = "left"


