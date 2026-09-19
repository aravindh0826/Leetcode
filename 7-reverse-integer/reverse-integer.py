class Solution(object):
    def reverse(self, x):
        if x < 0:
            a = str(x)
            b = a[1:]
            b = b[::-1]
            result = -int(b)
        else:
            a = str(x)
            b = a[::-1]
            result = int(b)
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result    