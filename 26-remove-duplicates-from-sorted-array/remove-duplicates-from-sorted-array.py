class Solution(object):
    def removeDuplicates(self, nums):
        num2=[]
        for i in nums:
            if i in num2:
                continue
            else:
                num2.append(i)
        nums[:]=num2
        
        