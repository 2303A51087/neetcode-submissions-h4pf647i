# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def traversal(root,res,depth):
            if root:
                if len(res)==depth:
                    res.append([])
                res[depth].append(root.val)
                traversal(root.left,res,depth+1)
                traversal(root.right,res,depth+1)

            
        res=[]
        traversal(root,res,0)
        return res
        