# LeetCode 94. Binary Tree Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Given the root of a binary tree,
return the inorder traversal of its nodes' values.
"""


# My initial, successful solution
def inorder_traversal(root):
    def traverse(node, values=[]):
        if node:
            traverse(node.left, values)
            values.append(node.val)
            traverse(node.right, values)
        return values
    return traverse(root)


# One-line solution from LC user 'wingkwong'
def one_line(root):
    return one_line(root.left) + [root.val] + one_line(root.right) if root else []
