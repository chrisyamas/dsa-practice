from stack import Stack


def are_brackets_balanced(string):
    """
    Function returns a boolean indicating whether all brackets (if any exist
    within input string) are part of a validly placed, matching pair.

    Params
    ------
    :string: any string-type object

    Return
    ------
    Boolean - False if any bracket is not validly matched, True otherwise
    """
    bracket_hash = {"{": "}", "[": "]", "(": ")"}
    stack = Stack()
    for char in string:
        # Push character to stack if it is opening-type bracket:
        if char in {"{", "[", "("}:
            stack.push(char)
        # If character is closing-type bracket:
        if char in {"}", "]", ")"}:
            # Return false if stack empty (no opening-types to match with):
            if stack.is_empty():
                return False
            # Otherwise, pop top value of stack, hold in current_char variable:
            current_char = stack.pop()
            # If char does not match current_char's key value in bracket_hash,
            # return false:
            if bracket_hash[current_char] != char:
                return False
    # If stack is not empty after string iteration complete, there is 1 or more
    # extra opening brackets in string, so function should return False:
    if not stack.is_empty():
        return False
    else:
        return True


if __name__ == '__main__':
    test_string = "{here we go again [testing strings (you know it!), bud]...}"
    result = are_brackets_balanced(test_string)
    print(result)

