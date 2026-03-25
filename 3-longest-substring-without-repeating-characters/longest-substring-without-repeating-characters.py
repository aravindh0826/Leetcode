class Solution(object):
    def lengthOfLongestSubstring(self,s):
        char_map = {}   
        left = 0
        max_length = 0

        for right, ch in enumerate(s):
            if ch in char_map and char_map[ch] >= left:
                left = char_map[ch] + 1 

            char_map[ch] = right
            max_length = max(max_length, right - left + 1)

        return max_length  