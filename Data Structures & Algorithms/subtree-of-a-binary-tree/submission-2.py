# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # we want to keep going until rootVal matches subRoot. if NONE of the rootVals match
        # subroot then return false

        def check(root,subroot):
            if not root:
                return False
            if root.val == subroot.val:
                return sameTree(root,subroot) or check(root.left,subroot) or check(root.right,subroot)
            else:
                return check(root.left,subroot) or check(root.right,subroot)

            
        # normal sameTree on subroot

        def sameTree(root,subRoot):
        
            # if we compare the roots of both, and they AREN'T true. we want to traverse.
            # lets say we compare 1 and 2. this isn't true.
            # we then want to check if 2 and 3 could be the roots of the subtree.
            # we find out that 2 IS the root of the subtree.
            # so then we start iterating from there.
            # we move both trees to the left and right pointer. if those are correct then we 
            # keep recursively checking. if the check up until that point is good, we'll return true.
            # by default, we'll keep it at False.
            if not root and not subRoot:
                return True
            elif (not root or not subRoot) or root.val != subRoot.val:# if either of them aren't valid but the other is
            # then its not valid
                return False
            else:# the "root" values are the same now, so we want to start moving the subTree
                return sameTree(root.left,subRoot.left) and sameTree(root.right,subRoot.right)

            """
            if (not subRoot or not root) or root.val != subRoot.val:
                return False

            left = sameTree(root.left, subRoot.left)
            right = sameTree(root.right, subRoot.right)
            
            return left and right
            """
        return check(root,subRoot)