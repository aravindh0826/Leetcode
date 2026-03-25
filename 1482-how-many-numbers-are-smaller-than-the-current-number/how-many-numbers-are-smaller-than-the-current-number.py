class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        nums2=sorted(nums)
        result=[]        
        for num in nums:
            result.append(nums2.index(num))     
        return result
                       