class Solution(object):
    def checkIfPangram(self, sentence):
        return len(set(sentence)) == 26
        
s= Solution()
print(s.checkIfPangram("leetcode"))
        