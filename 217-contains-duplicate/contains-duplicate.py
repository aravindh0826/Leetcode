class Solution(object):
    def containsDuplicate(self,nums):
        hashmap = {}

        for num in nums:
            if num in hashmap:
                return True
            hashmap[num] = 1

        return False
        