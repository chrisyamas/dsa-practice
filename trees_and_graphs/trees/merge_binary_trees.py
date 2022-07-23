# LeetCode problem 617. Merge Two Binary Trees

# My first (unsuccessful) attempt: needs to be revised
# for solution to compile properly

def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    # 1. If there is node for A and B -> sum node vals, add new node with
    # that val
    # 2. If node for just A -> add new node with that val
    # 3. If node for just B -> add new node with that val
    # 4. If no node for either A or B, return
    # I want to use depth-first, pre-order traversal
    # Conditionals include A+B, just A, just B, else
    # Will define the function within the mergeTrees func, and pass it
    # new_root

    def traverse(a, b, c, child_id=None):
        if a and b:
            new_val = a.val + b.val
        elif a:
            new_val = a.val
        elif b:
            new_val = b.val
        else:
            return
        new_node = TreeNode(new_val)
        if child_id == "left":
            c.left = new_node
        if child_id == "right":
            c.right = new_node
        traverse(a.left, b.left, new_node, "left")
        traverse(a.right, b.right, new_node, "right")

    if root1 and root2:
        merge_val = root1.val + root2.val
    elif root1:
        merge_val = root1.val
    elif root2:
        merge_val = root2.val
    else:
        return None

    merge_root = TreeNode(merge_val)
    traverse(root1.left, root2.left, merge_root, "left")
    traverse(root1.right, root2.right, merge_root, "right")
    return merge_root