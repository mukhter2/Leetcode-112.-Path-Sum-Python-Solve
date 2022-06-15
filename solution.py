# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sum=0
        def recurser(root,sum):
            if root is None:
                return 
            else:
                sum+=root.val
                if sum==targetSum and root.left is None and root.right is None:
                    return True
                f= recurser(root.left,sum)
                g=recurser(root.right,sum)
                if f or g:
                    return True
            return False
        val=recurser(root,sum)
        return val
