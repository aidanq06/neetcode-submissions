# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        tree1 = []
        tree2 = []

        def dfs1(root):
            if not root:
                tree1.append(None)
                return

            tree1.append(root.val)
            dfs1(root.left)
            dfs1(root.right)
        
        def dfs2(root):
            if not root:
                tree2.append(None)
                return

            tree2.append(root.val)
            dfs2(root.left)
            dfs2(root.right)
            
        
        dfs1(p)
        dfs2(q)

        print(tree1,tree2)
        
        return tree1 == tree2
        """

        """
        Attempt 2
        def dfs(p, q):

            # if either of them are uneven
            if (not p and q) or (not q and p):
                return False
            if not p and not q: # if BOTH of them are null then we'll return nothing
                return
            left = dfs(p.left,q.left)
            right = dfs(p.right,q.right)

            return left and right
        
        return dfs(p,q)
        """

        # attempt 3

        # we want to start with preorder traversal. comparing the first nodes we see

        def dfs(p,q):
            if not p and not q:
                return True
            
            # preorder
            if (not p or not q) or p.val != q.val:
                return False
            
            else:
                return dfs(p.left,q.left) and dfs(p.right,q.right)
        
        return dfs(p,q)


        