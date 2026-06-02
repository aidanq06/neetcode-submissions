# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # we essentially just want a standard bfs implementation

        # correction: we want level order traversal. levels actually matter in this situation
        
    
        if not root:
            return []

        queue = deque([root])
        final = []

        while queue:
            curr = []
            for _ in range(len(queue)):
                node = queue.popleft()
                curr.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            final.append(curr)
        return final
