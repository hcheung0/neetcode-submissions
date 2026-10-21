# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Recursion method
        if root == None: # Base case; the current node doesn't exist so we just return None
            return None
        else: # Recursive case, swap left and right and call invertTree on both
              # left and right nodes. Return current node as well
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root
            
        

            