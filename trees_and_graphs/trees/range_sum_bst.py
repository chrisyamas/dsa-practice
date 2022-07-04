# Definition for a binary tree node from LeetCode.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def range_sum_bst(root, low, high):
    """
    Given the root node of a binary search tree and two integers low and high,
    return the sum of values of all nodes with a value
    in the inclusive range [low, high].
    """
    # Here is LeetCode's iterative implementation.
    # But below it is their recursive implementation.
    # It does not perform nearly as well, for either time or space.
    # This iterative approach uses an array-based stack, but a node-based stack
    # would work well to (and I believe a node-based queue would as well,
    # as in breadth-first search)
    ans = 0
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            if low <= node.val <= high:
                ans += node.val
            if low < node.val:
                stack.append(node.left)
            if node.val < high:
                stack.append(node.right)
    return ans


def range_sum_bst_recursive(root, low, high):
    def dfs(node):
        nonlocal ans
        if node:
            if low <= node.val <= high:
                ans += node.val
            if low < node.val:
                dfs(node.left)
            if node.val < high:
                dfs(node.right)
    ans = 0
    dfs(root)
    return ans
