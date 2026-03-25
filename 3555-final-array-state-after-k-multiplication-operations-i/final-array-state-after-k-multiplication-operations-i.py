class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        for i in range(k):
            x=min(nums)
            y=nums.index(x)
            nums[y]=x*multiplier
        return nums
        