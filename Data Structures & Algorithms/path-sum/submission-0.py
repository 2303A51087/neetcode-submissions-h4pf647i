# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root==None :
            return False 
        d=deque([[root,root.val]])
        while d:
            node,cur_sum=d.popleft()
            if node.left==None and node.right==None and cur_sum==targetSum:
                return True 
            if node.left:
                d.append([node.left,cur_sum+node.left.val])
            if node.right:
                d.append([node.right,cur_sum+node.right.val])
        return False



        