# LeetCode Problem 19. Remove Nth Node From End of List
# My solution using one pointer, two passes

def remove_nth_from_end(head, n):
    """
    Given the head of a linked list, remove the nth node from the end of the
    list and return its head.

    Example 1:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

    Example 2:
    Input: head = [1], n = 1
    Output: []
    """
    current = head
    length = 0

    while current:
        length += 1
        current = current.next

    target = length - n

    if target == 0:
        head = head.next

    count = 0
    current = head

    while current:
        count += 1
        if count == target:
            current.next = current.next.next
            break
        current = current.next

    return head


# ---ALGORITHM---
    # First solution: two subsequent traversals
    # When I remove, I will want to have access to node right before node being removed
    # so I can reassign its .next to be its current next.next
    # First traversal purpose: get length of list
    # Second traversal purpose: remove node
    # For first traversal, initialize current = head, length = 0
    # While current, increment length by 1 and assign current to current.next
    # After first traversal, set target equal to length - n
    # Initialize count variable at zero
    # Reassign current to head
    # Run second traversal like first (while loop), but increment count by 1
    # On each iteration, after incrementing count, conduct check to see if
    # count == target. If it does, reassign current.next to be current.next.next
    # Return head
