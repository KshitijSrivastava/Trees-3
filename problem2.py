

## Problem2 (https://leetcode.com/problems/symmetric-tree/)

#recursive code
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def symm(root1, root2):
            if root1 is None and root2 is None:
                return True
            elif root1 is None and root2 is not None:
                return False
            elif root1 is not None and root2 is None:
                return False
            elif root1.val != root2.val:
                return False
            
            #when both the nodes have equal value
            #see both the subtrees are same
            return symm(root1.left, root2.right) and symm(root1.right, root2.left)
        
        
        return symm(root.left, root.right)


# Iterative code
class Solution:
    def get_BFS(self, root, direction = "L"):
        output = []
        queue = []
        queue.append(root)
        
        while len(queue) != 0:
            node = queue.pop(0)
            
            if node is None:
                output.append(None)
                continue
            
            output.append(node.val)
            
            if direction == "L":
                queue.append(node.right)
                queue.append(node.left)
            else:
                queue.append(node.left)
                queue.append(node.right)
                
        return output
        
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        left_root = root.left
        left_arr = self.get_BFS(left_root, "L")
        right_root = root.right
        right_arr = self.get_BFS(right_root, "R")
        
        # print(left_arr)
        # print(right_arr)
        
        if len(left_arr) != len(right_arr):
            return False
        
        for l, r in zip(left_arr, right_arr):
            if l != r:
                return False
        return True
