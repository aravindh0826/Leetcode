class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        m=0
        current=0
        for ch in s:
            if ch=="(":
                current+=1
                m=max(current,m)
            elif ch==")":
                current-=1
        return m
        