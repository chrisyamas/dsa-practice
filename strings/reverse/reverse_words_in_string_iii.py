

def reverse_words(s):
    """
    Given a string s, reverse the order of characters in each word within a
    sentence while still preserving whitespace and initial word order.

    Example 1:

    Input: s = "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"
    """
    s_list = s.split()
    new_s = ""

    for i in range(len(s_list)):
        char_index = len(s_list[i]) - 1
        while char_index >= 0:
            new_s += s_list[i][char_index]
            char_index -= 1
        if i < len(s_list) - 1:
            new_s += " "
    return new_s
