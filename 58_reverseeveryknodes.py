'''
Given the head of a linked list, reverse the nodes of the list k at a time, 
and return the modified list.
k is a positive integer and is less than or equal to the 
length of the linked list. If the number of nodes is not a multiple of 
k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.'''

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reversell(start, k):
            prev, cur = None, start
            while cur and k:
                next_node = cur.next
                cur.next = prev
                prev = cur
                cur = next_node
                k -= 1
            return prev
        temp = head
        count = 0
        while temp and count < k:
            temp = temp.next
            count += 1
        if count == k:
            new_head = reversell(head, k)
            head.next = self.reverseKGroup(temp, k)
            return new_head
        return head