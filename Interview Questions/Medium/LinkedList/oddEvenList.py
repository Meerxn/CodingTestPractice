
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        dummyHead1 = even = ListNode(0)
        dummyHead2 = odd = ListNode(0)
        curr = head
        while curr:
            odd.next = curr
            even.next = curr.next
            odd = odd.next
            even = even.next
            if even:
                curr = curr.next.next
            else:
                curr = None
        odd.next = dummyHead1.next
        return dummyHead2.next
            
        
        