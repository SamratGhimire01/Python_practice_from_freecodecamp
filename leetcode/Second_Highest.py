# def second_largest(data):
#     largest  = second = -1
    
#     for i in data:
#         if i > largest:
#             second = largest
#             largest = i
#         elif i>second and i<largest:
#             second = i
#     if second == largest:
#         return -1
#     return second

    
# print(second_largest(  [12, 35, 1, 10, 34, 1]))


class Solution(object):
    def secondHighest(self, s):
        d = set()
        for i in s:
            if i.isdigit():
                d.add(int(i))
            else:
                continue
        largest  = second = -1
        
        for i in d:
            if i > largest:
                second = largest
                largest = i
            elif i>second and i<largest:
                second = i
    
        return second if second != -1 else -1

s= Solution()
print(s.secondHighest("dfa12321afd"))
        