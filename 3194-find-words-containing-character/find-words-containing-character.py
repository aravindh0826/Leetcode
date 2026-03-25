class Solution(object):
    def findWordsContaining(self, words, x):
        y=[]
        for i in range(len(words)):
            if x in words[i]:
                y.append(i)
        return y
