# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # brute force solution would be to add all the values in both lists to a normal list, then sorting the list
        # then converting it back into a linkedlist (would be O(n) space)
        # consolidate everything into list1

        # we need to use dummyNode
        # listnode objects are immutable, you can change them after creation

        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1: # we want to add at the end if it ISN'T null even after one of the lists reach the end
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next
        
        
        # this implementation essentially adds 0 to the first list
        # 0 -> 1 -> 2 -> 4
        # ^

        # important when the head might change
        """
        while not list1 and not list2: # UNTIL both linkedlists are NONE
            if list1 and list2: # both have valid heads
                if list1.val > list2.val:
                    temp = list2.next
                    list2.next=list1
                    list2=temp
                if list2.val < list1.val:
                    temp = list1.next
                    list1.next=list2
                    list1=temp
                if list1.val == list2.val
                    temp = list1.next
                    list1.next = list2
                    list1=temp
            if not list1 and list2: # list1 curr is empty
        
        return 
        """
            

