from tree_node import TreeNode


def dfs(root, search_value):
    """
    Using pre-order traversal to find input search value.
    """
    if root:
        if root.value == search_value:
            return root
        return dfs(root.left) or dfs(root.right)
    return None
