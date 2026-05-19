# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        # brute force is to keep a "seen" set
        # and iterate through
        # this however is O(n) space

        curr = head
        seen = set()

        while curr:
            if curr.next not in seen:
                seen.add(curr)
            elif curr.next in seen:
                return True
            curr=curr.next
        
        return False
        """

        # official solution is a fast and slow pointer approach. 
        # if there actually WAS a cycle then the fast pointer will eventually overlap the slow pointer

        
        slow = head
        fast = head

        while fast and fast.next: # if the fast REACHES a none, then that means its NOT a loop
            
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
