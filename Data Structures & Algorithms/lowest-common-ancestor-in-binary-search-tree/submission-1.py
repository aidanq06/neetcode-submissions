# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # brute force, we can keep "Updating" the lowest common ancestor
        # lets say in the example, at 5. we check, is 3 and 8 ancestors? yes?
        # then we update the lowest common ancestor to be 5.
        # we then check the children of 5.
        # is 3 an ancestor of 3? yes.
        # is 8 an ancestor of 3? no.
        # is 8 an ancestor of 8? yes.
        # is 3 an ancestor of 3? no.
        # from here, we can stop checking further. 

        # on second thought, lets reset how we think.
        # lets say p = 4 and q = 9
        # the lowest common ancestor is still 5.
        # lets check starting with the node. 
        # thinking of layer by layer, my intuition is dfs. 
        # the solution should be in O(h) time and O(h) space which usually implies a dfs solution

        # im thinking about the fact that its a binary search tree.
        # i know that a binary search tree starts with a node. its right value is greater, the left value is lesser.

        # in the given solution, the max amount of operations it should take is 4.

        # the node is ALWAYS going to be the greatest ancestor
        # so we start from there
        # lets say we're looking for lowest common ancestor of 7 and 9.
        # 3 is it a common ancestor of either? no
        # 8 is it an ancestor of either? yes

        # new thought
        # in a binary search tree, left is less than, right is greater than.
        # think. 3 is LESS than 5 therefore it has to be on the left. 8 is GREATER than 5 so it has to be on the right.
        # therefore 5 at that point HAS to be the lowest common ancestor. we can just cut it off there. 
        
        # case 2: p = 3, q = 4. node is 5.
        # both of them are smaller than 5. therefore we have to the left.
        # 3 == 3? yes, so that means that has to be the lowest common ancestor. no matter what.
        # if p == node.val or q == node.val:
        #   return node.val

        def dfs(root):
            if not root:
                return

            if (root.val > p.val and root.val < q.val) or (root.val > q.val and root.val < p.val): # if they are on both sides, the greatest common ancestor just has to be that.
                return root
            elif root.val > p.val and root.val > q.val: # greater than both, that means we have to go left 
            # e.g. 3 and 4 when root is 5
                return dfs(root.left)
            elif root.val < p.val and root.val < q.val:
                return dfs(root.right)
            elif root.val == p.val or root.val == q.val:
                return root

        return dfs(root)