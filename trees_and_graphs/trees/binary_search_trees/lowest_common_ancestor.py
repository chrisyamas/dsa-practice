# LeetCode Problem 235. Lowest Common Ancestor of a Binary Search Tree


def lowest_common_ancestor(root, p, q):
    # Algorithmic explanation from LeetCode:

    # 1. Start traversing the tree from the root node.
    # 2. If both the nodes p and q are in the left subtree, then continue
    # the search with left subtree starting step 1.
    # 3. If both the nodes p and q are in the right subtree, then continue
    # the search with right subtree starting step 1.
    # If both step 2 and step 3 are not true, this means we have found
    # the node which is common to node p's and q's subtrees, and hence we
    # return this common node as the LCA.

    # My solution
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    elif p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)
    else:
        return root
