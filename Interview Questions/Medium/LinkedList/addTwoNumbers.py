        head = ListNode(0,None)
        l3 = head
        carry = 0 
        while l1 or l2 or carry:
            val1 = 0 
            val2 = 0 
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            sumVal = val1 + val2 + carry
            if sumVal >= 10:
                carry = 1
                sumVal = sumVal % 10
            else:
                carry = 0 
            l3.next = ListNode(sumVal,None)
            l3 = l3.next
        return head.next
                