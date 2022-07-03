
def reverse_linked_list_recursive(head):
    """
    From LeetCode:
    Intuition
    ---------
    The recursive version is slightly trickier and the key is to work
    backwards. Assume that the rest of the list had already been reversed,
    now how do we reverse the front part? Let's assume the list is:
    n1 → … → nk-1 → nk → nk+1 → … → nm → Ø

    Assume from node nk+1 to nm had been reversed, and we are at node nk.
    n1 → … → nk-1 → nk → nk+1 ← … ← nm

    We want nk+1’s next node to point to nk. So,
    nk.next.next = nk

    Be very careful that n1's next must point to Ø. If you forget about this,
    your linked list will have a cycle in it. This bug could be caught if you
    test your code with a linked list of size 2.
    """
    if not head or not head.next:
        return head

    rest = reverse_linked_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return rest
