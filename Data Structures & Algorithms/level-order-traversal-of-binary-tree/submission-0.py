# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        finalans = [[root.val]]
        stack = collections.deque()
        stack.append(root)

        while stack:
            dummy = []
            for _ in range(len(stack)):
                node = stack.popleft()
                if node.left:
                    dummy.append(node.left.val)
                    stack.append(node.left)
                if node.right:
                    dummy.append(node.right.val)
                    stack.append(node.right)
            if dummy:
                finalans.append(dummy)
        
        return finalans


        