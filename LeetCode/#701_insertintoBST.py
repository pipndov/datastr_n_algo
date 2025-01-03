# You are given the root node of a binary search tree (BST) and a 
# value to insert into the tree. 
# Return the root node of the BST after the insertion. 
# It is guaranteed that the new value does not exist 
# in the original BST.

# Definition for a binary tree node.

# ************************************************************************************************************************************************

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:                
            return TreeNode(val)                                    # base case (if current node is none) a new tree node is made
        if root.val < val:                                          # if val is greater than root.val
            root.right = self.insertIntoBST(root.right, val)        # recursively searches in the right subtree
        elif root.val > val:                                        # if val is less than root.val
            root.left = self.insertIntoBST(root.left, val)          # recursively searches in the left subtree
        return root     # rebuilds Tree each recursion
    
    # if an empty spot (None) is found, we create and insert a new (TreeNode) with the value (val)