class Solution(object):
    def reverseBits(self, n):
        b_num = list(f'{n:032b}')
        for i in range(16):
            tem=b_num[i]
            b_num[i] = b_num[-1-i]
            b_num[-1-i] = tem
        return int("".join(b_num),2)
        
            
s=Solution()
print(s.reverseBits(2147483644))
