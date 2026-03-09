class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.split()
        if not s:
            return 0
        return len(s[-1])

s_obj = Solution()
print(s_obj.lengthOfLastWord("   fly me   to   the moon  "))
