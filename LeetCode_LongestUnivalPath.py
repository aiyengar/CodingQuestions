# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        
        def longestUnivalPathUtil(node):
            if not node:
                return 0

            leftVal = longestUnivalPathUtil(node.left)
            rightVal = longestUnivalPathUtil(node.right)

            leftMax = 0
            rightMax = 0

            if node.left and node.val ==  node.left.val:
                leftMax = leftVal + 1

            if node.right and node.val == node.right.val:
                rightMax = rightVal + 1

            self.ans = max(self.ans,leftMax + rightMax)
            return max(leftMax,rightMax)
        
        longestUnivalPathUtil(root)
        return self.ans
