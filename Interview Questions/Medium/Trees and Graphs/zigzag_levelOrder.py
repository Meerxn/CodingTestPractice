class Solution:
    #NOT DONE YET -- NEEDS FIXING
    '''
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
                '''
                 if root is None:
        return
    s1 = []
    s2 = []
    s1.append(root)
    result = []
    curr_res = []
    while (s1 or s2):
        while (len(s1) > 0):
            curr = s1[-1]
            curr_res.append(curr.data)
            s1.pop()

            if (curr.left):
                s2.append(curr.left)
            if (curr.right):
                s2.append(curr.right)
            if (len(s1) == 0):
                result.append(curr_res)
                curr_res = []
        while (len(s2) > 0):
            curr = s2[-1]
            curr_res.append(curr.data)
            s2.pop()
            if (curr.right):
                s1.append(curr.right)
            if (curr.left):
                s1.append(curr.left)
            if (len(s2) == 0):
                result.append(curr_res)
                curr_res = []
    return result


