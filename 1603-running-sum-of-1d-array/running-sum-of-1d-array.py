class Solution(object):
    def runningSum(self, nums):
        runningsum=0
        l2=[]
        for i in nums:
            runningsum+=i
            l2.append(runningsum)
        return l2
        