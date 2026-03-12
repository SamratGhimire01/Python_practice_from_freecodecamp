class Solution(object):
    def bitwiseComplement(self, n):
        n= list(bin((n))[2:])
        for i in range(len(n)):
            if n[i]=='1':
                n[i] = '0'
            else:
                n[i] ='1'
        return int(''.join(n),2)
        

s=Solution()
print(s.bitwiseComplement(5))
        