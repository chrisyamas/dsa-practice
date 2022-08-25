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


# Quicker approach (Two Pointers in array/list):
# traverses linked list, makes list of values, use two pointers in list,
# works inward comparing values.
def two_pointers_is_palindrome(head):
    values = []
    current = head

    while current:
        values.append(current.val)
        current = current.next

    low = 0
    high = len(values) - 1

    while low < high:
        if not values[low] == values[high]:
            return False

    return True


# Simpler syntax version of above solution:
def simpler_two_pointers_is_palindrome(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values == values[::-1]

