class Solution(object):
    def prefixCount(self,names, queries):
        count = 0
        for name in names:
            if name.startswith(queries):
                count += 1
        
        return count
        