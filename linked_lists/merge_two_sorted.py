# Definition for singly-linked list from LeetCode.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def merge_two_sorted_lists(list1, list2):
    if not list1:
        return list2
    elif not list2:
        return list1
    # The idea behind the next two conditional is that the node with the lowest
    # value should be put first, and that should continue to be executed
    # recursively (until the end of a list is reached, which is handled by the
    # above base cases)
    elif list1.val < list2.val:
        list1.next = merge_two_sorted_lists(list1.next, list2)
        return list1
    else:
        list2.next = merge_two_sorted_lists(list1, list2.next)
        return list2
