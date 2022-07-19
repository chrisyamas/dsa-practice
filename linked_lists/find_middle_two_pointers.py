# LeetCode 876. Middle of Linked List
# My solution using TWO pointers and ONE pass

def find_middle_two_pointers(head):
    # Two Pointers, One Loop
    first = head
    second = head
    while second and second.next:
        first = first.next
        second = second.next.next
    return first
