# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # [5,3,9,1,4]
        # val = 6
        # essentially we're start with the root. 
        # if we do root.val its 5 (this is the top)
        # we compare root.val to val. if val is larger than root.val, move to the right, if its less than, move to the left.
        # 6 is greater than 5, so we move down to 9. 
        # we do the same thing. in this case, 6 is LESS than 9, so we're going to CHECK if its null first, if its not null then move to the left.
        # since left of 9 IS NULL, we want to return TreeNode(6) for that 
        

        def insert(curr, val):
            # if the node we're at is Null THATS when we want to "insert"
            if not curr:
                return TreeNode(val)

            if val>curr.val:
                curr.right = insert(curr.right,val)
            if val<curr.val:
                curr.left = insert(curr.left,val)
            
            return curr

        
        return insert(root,val)