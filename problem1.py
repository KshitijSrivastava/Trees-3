## Problem1 (https://leetcode.com/problems/path-sum-ii/)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        #to store the final output
        output = []
        
        def path(root, targetSum, currSum, curr_arr):
            #is root is null return
            if root is None:
                return
            
            #if its a leaf node then check if the current sum is equal to the target
            if root.left is None and root.right is None:
                curr_arr.append( root.val )
                
                nonlocal output
                currSum  = currSum + root.val
                if currSum == targetSum:
                    output.append( curr_arr[::] )
                
                curr_arr.pop()
                return
            
            #Go over left root
            curr_arr.append( root.val )
            path( root.left, targetSum, currSum + root.val, curr_arr )
            curr_arr.pop()
            
            #Go over right root
            curr_arr.append( root.val )
            path( root.right, targetSum, currSum + root.val, curr_arr )
            curr_arr.pop()
            
        path(root, targetSum, 0, [])
        
        return output