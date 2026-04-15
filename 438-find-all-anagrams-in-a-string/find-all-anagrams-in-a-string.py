class Solution(object):
    def findAnagrams(self, s, p):
        res = []
        k = len(p) 
        if len(s) < k:
            return res  
        p_count = [0] * 26
        window_count = [0] * 26
        for i in range(k):
            p_count[ord(p[i]) - ord('a')] += 1
            window_count[ord(s[i]) - ord('a')] += 1
        if window_count == p_count:
            res.append(0)
        for i in range(k, len(s)):
            window_count[ord(s[i]) - ord('a')] += 1        
            window_count[ord(s[i - k]) - ord('a')] -= 1         
            if window_count == p_count:
                res.append(i - k + 1)  
        return res