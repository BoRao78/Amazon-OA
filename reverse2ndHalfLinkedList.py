class Solution:
    def reverse2ndHalf(self, head):
        p1 = head
        p2 = head
        p3 = p2
        counter = 0
        while(p1 != None):
            p1 = p1.next
            counter += 1
            if(counter % 2 == 0):
                p3 = p2
                p2 = p2.next
        
        p2 = self.reverse(p2)
        p3.next = p2
        return head

    def reverse(self, head):
        curr = head
        prev = None
        while curr is not None:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        head.next = None
        return prev