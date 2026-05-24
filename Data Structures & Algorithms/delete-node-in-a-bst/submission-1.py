# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findMin(root):
            while root and root.left:
                root = root.left
            return root.val

        
        # 2 cases:

        # 1st case is that theres either 0 or 1 child, in that case, it will be much simpler
        # if theres 0 children (leaf node) then we can just set the parent.left or parent.right to Null
        # if theres 1 child, we can point the parent.left to child

        # 2nd case is that theres 2 or more children, in that case it will be more difficult
        # lets see 3 in the first graph
        # 3 is connected to 1 and 4
        # in this case, we want to use the min of the right OR the max of the left. see 1 and 4. 
        # We'll pick the least of them to replace 3. 

        # we'll replace 3 with 4 since 4 is the min of the right sub tree
        # we also have to actually get rid of 4 since it needs to be Null

        #.   5
        #. 4   9
        # 1    
        
        def delete(root,key):
            #first we need to account for if root is actually valid

            if not root:
                return None

            # we first have to "FIND" where the key is
            if key>root.val:
                root.right = delete(root.right,key)
            elif key<root.val:
                root.left = delete(root.left,key)
            elif key==root.val: # found it
                if not root.left and not root.right: # 0 children
                    return None
                if not root.left or not root.right: # 1 child
                    if root.left:
                        return root.left
                    if root.right:
                        return root.right
                if root.left and root.right: # 2 children
                    minimum = findMin(root.right)
                    root.val = minimum
                    root.right = delete(root.right,minimum)
            return root
    

        return delete(root,key)