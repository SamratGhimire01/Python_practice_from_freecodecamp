# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         return bin(int(a,2)+int(b,2))[2:]
# s= Solution()
# print(s.addBinary(a = "11", b = "1"))


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len= len(a) if len(a) > len(b) else len(b)
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        rem=[0]
        result=[]
        for i in range(-1, -max_len - 1, -1):
            # Fix 4: Use string "0" and "1" (input is string)
            if a[i] == "0" and b[i] == "0":
                if rem.pop() == 1:
                    result.append("1")
                else:
                    result.append("0")
                rem.append(0)
            elif a[i] == "1" and b[i] == "1":
                if rem.pop() == 1:
                    result.append("1")
                else:
                    result.append("0")
                rem.append(1)
            elif (a[i] == "0" and b[i] == "1") or (a[i] == "1" and b[i] == "0"):
                if rem.pop() == 1:
                    result.append("0")
                    rem.append(1)
                else:
                    result.append("1")
                    rem.append(0)
        if rem.pop() == 1:
            result.append('1')
        result.reverse()
        return str("".join(result))
                
                    
                
                                 
s= Solution()
print(s.addBinary(a = "11", b = "1"))