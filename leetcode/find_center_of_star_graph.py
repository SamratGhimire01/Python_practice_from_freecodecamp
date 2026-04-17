class Solution(object):
    def findCenter(self, edges):
        if edges[0][0] in edges[1]:
            return edges[0][0]
        return edges[0][1]
        
s = Solution()
print(s.findCenter([[1,2],[2,3],[4,2]]))
