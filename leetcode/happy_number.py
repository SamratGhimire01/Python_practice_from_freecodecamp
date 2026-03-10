class Solution(object):
    def isHappy(self, n):
        result= {'0':0,'1':set()}
        while True:
            result['0']=0
            num = str(n)
            for i in range(len(str(n))):
                result['0'] += (int(num[i])*int(num[i]))
            
            if result['0'] ==1:
                return True
            if result['0'] in result['1']:
                return False
            result['1'].add(result['0'])
            n=result['0']
        
s= Solution()
print(s.isHappy(19))