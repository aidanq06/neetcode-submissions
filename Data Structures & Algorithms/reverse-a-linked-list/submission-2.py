# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # when im first looking at this problem, my first instinct is to go for a brute force solution
        #
        # My first thought is to iterate through the given linkedlist, head, appending each item to a 
        # normal list. Reversing that normal list, then returning a new linkedlist appending the items in
        # the normal list to the linkedlist

        # however we see that the given space complexity is O(1)
        # therefore we can't "create" a new list. we need to work with what we're given

        
        # None -> 0 -> 1 -> 2 -> 3 -> None
        #.        ^
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr

            curr = temp
            """
            if curr.next:
                temp = curr.val
                curr.val = curr.next.val
                curr.next.val = temp 
            """
        return prev
    
        # we need to return prev since the entirety of the linkedlist is stored off prev
        # curr is going to be None, since after the list is complete curr is always going to be none
        # we shouldn't return curr after running a while loop like that
            



        

            
