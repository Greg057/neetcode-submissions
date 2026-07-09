# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.equivalent = True

        def dfs(p, q):
            if q and not p or p and not q:
                self.equivalent = False
                return

            if not q and not p:
                return
            
            if q.val != p.val:
                self.equivalent = False
                return

            left = dfs(p.left, q.left)
            right = dfs(p.right, q.right)

        dfs(p, q)
        return self.equivalent

        