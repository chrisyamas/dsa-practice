# LeetCode problem 412. Fizz Buzz
# My solution below


def fizzBuzz(self, n: int) -> List[str]:
    fb_list = []
    for i in range(1, n + 1):
        if not i % 3 and not i % 5:
            fb_list.append("FizzBuzz")
        elif not i % 3:
            fb_list.append("Fizz")
        elif not i % 5:
            fb_list.append("Buzz")
        else:
            fb_list.append(str(i))
    return fb_list