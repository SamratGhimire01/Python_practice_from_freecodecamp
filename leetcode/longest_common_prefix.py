class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        a=''
        for i in range(len(strs[0])+1):
            if not all(strs[0][:i] == x[:i] for x in strs):
                
                return a
            a=strs[0][:i]
        return a     
s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))