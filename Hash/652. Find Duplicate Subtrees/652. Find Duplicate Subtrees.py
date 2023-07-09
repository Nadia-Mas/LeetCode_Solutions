import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findDuplicateSubtrees(self, root:list[TreeNode]) -> list[list[TreeNode]]:
        def traverse(node):
            if not node:
                return ""
                                        
            representation = ("(" + traverse(node.left) + ")" + str(node.val)
                              + "(" + traverse(node.right) + ")")
            
            cnt[representation] +=1
            if cnt[representation]==2:
                res.append(node)
            return representation
                
        cnt = collections.defaultdict(int)
        res = []
        traverse(root)
        return res