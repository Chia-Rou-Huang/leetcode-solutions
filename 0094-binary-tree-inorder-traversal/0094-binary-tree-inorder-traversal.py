# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            res = [] 
            def traverse(node):
                # 停止條件：如果這格沒東西（null），就直接回頭
                if not node:
                    return
                traverse(node.left)
            
                res.append(node.val)
            
                traverse(node.right)
            
            traverse(root)
        
            return res
        