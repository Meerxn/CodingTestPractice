# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr = head
        length = 0
        while(curr != None):
            curr = curr.next
            length+=1
        print(length)
        index = 0
        curr = head
        if length == 1:
            head = None
            return head
        if n == length:
            head = head.next
            return head
        while(index < length):
            if index == length - n - 1:
                curr.next = curr.next.next
                break
            curr = curr.next
            index +=1
        return head