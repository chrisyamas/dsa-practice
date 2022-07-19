# LeetCode 876. Middle of Linked List
# My solution using ONE pointer and TWO pass

def find_middle_one_pointer(head):
    # One Pointer, Two Loops
    current = head
    length = 0

    while current:
        length += 1
        current = current.next

    middle_index = length // 2
    count = 0
    current = head

    while current:
        if count == middle_index:
            break
        current = current.next
        count += 1

    return current