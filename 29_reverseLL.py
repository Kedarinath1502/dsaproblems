'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''
# class Solution(object):
#     def reverseList(self, head):
#         if head is None or head.next is None :
#             return head
#         prev = head
#         head = head.next
#         prev.next = None
#         if head.next is None:
#             head.next = prev
#             return head
#         while head.next is not None:
#             after = head.next
#             head.next = prev
#             prev = head
#             head = after
#         head.next = prev
#         return head

class Solution(object):
    def reverseList(self, head):
        curr, prev = head, None
        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        return prev
    