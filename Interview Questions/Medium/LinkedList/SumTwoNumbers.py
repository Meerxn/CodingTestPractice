# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0,None)
        l3 = head
        
        while(True):
            
            
            if l1 == None:
                val1 = 0
            else:
                val1 = l1.val
                
            if l2 == None:
                val2 = 0 
            else:
                val2 = l2.val
            res = l3.val + val1 + val2
            l3.val = res%10  
            if l1 != None:
                
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
                
                
           
                    
            if l1 == None and l2 == None:
                if res > 9:
                    l3.next = ListNode(1,None)
                    
                break
            else:
                if res > 9:
                    l3.next = ListNode(1,None)
                else:
                    l3.next = ListNode(0,None)
                l3 = l3.next
                    
            
                
        return head
            
            
        