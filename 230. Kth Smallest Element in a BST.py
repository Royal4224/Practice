# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root, k: int) -> int:
        val, k = self.helper(root, k)
        return val

    def helper(self, root, k):
        if root is None:
            return root, k

        val, k = self.helper(root.left, k)
        if val is not None:
            return val, k

        if k == 1:
            return root.val, k

        val, k = self.helper(root.right, k - 1)
        return val, k
