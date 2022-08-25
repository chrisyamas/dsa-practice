# LeetCode 234. Palindrome Linked List

"""
Given the head of a singly linked list, return true if it is a palindrome.
"""


# My brute force, initial approach (reversed copy of array/list):
# traverses linked list, makes list of values, makes reverse copy
# and compares two lists for equivalency.
def reverse_list_is_palindrome(head):
    current = head
    values = []
    while current:
        values.append(current.val)
        current = current.next

    reverse_values = list(reversed(values))
    if values == reverse_values:
        return True

    return False

