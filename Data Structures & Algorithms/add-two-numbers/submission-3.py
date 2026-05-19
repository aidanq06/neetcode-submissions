# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # brute force solution would be to 
        # convert both linkedlists into normal list
        # reverse both of them
        # add the numbers in each
        # reverse that list
        # convert it back to linkedlist

        # lists have different lengths

        # O(n+m) time and O(1) space solution

        # [1,2,3] list a (321)
        # [4,5,6,7,8] list b (87654)
        # combined would be 87975
        # actual would be [5,7,9,7,8]

        # 1st: reverse both lists

        """
        prevL1 = None
        curr = l1
        while curr:
            temp = curr.next
            curr.next = prevL1
            prevL1 = curr
            curr = temp
        
        prevL2 = None
        curr = l2
        while curr:
            temp = curr.next
            curr.next = prevL2
            prevL2 = curr
            curr = temp


        
        # prev has the linkedlist reversed

        dummy = ListNode()
        tail = dummy

        # 0 -> 5
        carry = 0
        while l1 or l2 or carry:
            if prevL1:
                val1 = prevL1.val
            else:
                val1 = 0
            if prevL2:
                val2 = prevL2.val
            else:
                val2 = 0
            total = val1 + val2 + carry
            if (total) <= 9:
                tail.next = ListNode(total)
                carry=0
            if (total) > 9:
                tail.next = ListNode(total%10)
                carry = total//10
            if prevL2:
                prevL2 = prevL2.next
            if prevL1:
                prevL1 = prevL1.next
            tail = tail.next


            else:
                if (prevL2.val + prevL1.val + tail.next.next.val) < 9:
                    tail.next = ListNode(prevL2.val+prevL1.val+tail.next.next.val)
                elif (prevL2.val + prevL1.val + tail.next.next.val) > 9:
                    tail.next = ListNode((prevL2.val+prevL1.val+tail.next.next.val)//10)
                    tail.next.next = ListNode((prevL2.val+prevL1.val+tail.next.next.val))


            if prevL2.val + prevL2.val and curr.next # if the added values are greater than 9 and there exists 
            # a next number
                curr.next


        prev = None
        curr = dummy.next

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp


        return prev
        """

        dummy = ListNode()
        curr = dummy
        carry = 0
        
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            # 15 
            carry = val // 10
            val = val % 10 
            curr.next = ListNode(val)

            # updating pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next


        