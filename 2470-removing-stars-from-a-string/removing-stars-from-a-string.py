class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        s2=[]
        for i in s:
            if i=="*":
                s2.pop()
            else:   
                s2.append(i)
        return "".join(s2)
            

