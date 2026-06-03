# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # binary search tree def
        # given node:
        # the left node is going to be LESS than the node
        # the right node is going to be MORE than the node
        # we basically always want to carry a true or false
        # if at ANY POINT its false, we want to make sure it gets returned to the main.
        # If a value in the right subtree at any point is less than the parent node, then its NOT valid.
        

        # in EVERY left and right subtree of node, we need to make sure that not only its neighbors are good, but its 
        # children are good too.
        

        # essentially we need to recursively check if each neighbor on the left and right is good.
        # if it is good, then we'll return True. if not, we'll return False.

        # restart.

        # essentially, a binary search tree is. 
        # when you're given a root node, you're going to analyze the left and right children of that node.
        # if the left is LESS than the root node, and the right is MORE than the root node, that specific node is good
        # we then move to the left and right nodes, and repeat the same thing

        """
        self.rootNode = root.val
        def dfs(root):

            if not root:
                return True

            left = dfs(root.left)
            right = dfs(root.right)

            # if both children exist, check if the left is correct and right is correct
            if root.left and root.right:
                if (root.left.val < root.val and root.right.val > root.val):
                #(root.left.val < self.rootNode and root.right.val > self.rootNode):
                    return True
                else:
                    return False
            # if left exists and not right, we want to check left
            elif root.left and not root.right:
                if root.left.val < root.val and root.left.val < self.rootNode:
                    return True
                else:
                    return False
            # if right exists and not left, we want to check right
            elif root.right and not root.left:
                if root.right.val > root.val and root.right.val > self.rootNode:
                    return True
                else:
                    return False

            return left and right

            # problem with this specific testcase
            # root=[5,4,6,null,null,3,7]
            # at node 6, the children are 3, 7. its validating to be true.
            # HOWEVER 3 CANNOT be on the right side of the node because 3 is less than 5.
            # we need to always keep in mind of the root node. 

                    #5
                #4     #6
                    #3     #7
                    #^
            
            # if the current node (lets pretend its at 6) is greater than the root node, 
            # but its less than both 5 and 6, then its at the wrong place. 

            
            if left and right: 
                print("hi")
                return root.val

            if root.val > left and root.val < right:
                return True

            

            return dfs(root)
            print(root.val)

            if root.left:
                return root.left.val < root.val
            if root.right:
                return root.right.val > root.val
        """
        
        # complete restart
        # after getting hint:
        # we want to recursively user dfs which we were thinking of in the first place
        # HOWEVER, in each we want to provide a proper range. a min and a max using
        # < and >
        # at the root node, this is true. -inf < 5 < inf
        # then for the left child, now NO numbers on the left can be greater than 5
        # -inf < x < 5
        # for the right child, now NO numbers on the right can be LESS than 5. 
        # 5 < x < inf
        # we then recursively go through each node, passing along this equality expression. if any of them fail it
        # then we return False
            
        left = float("-inf")
        right = float("inf")

        def dfs(root, leftLimit, rightLimit):
            if not root:
                return True
            # if the root.val is within limits then its good
            if root.val > leftLimit and root.val < rightLimit:
                left = dfs(root.left, leftLimit, root.val)
                right = dfs(root.right, root.val, rightLimit)

                return left and right
            else:
                return False


        return dfs(root, left, right)