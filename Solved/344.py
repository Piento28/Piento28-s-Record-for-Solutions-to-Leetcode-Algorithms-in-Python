# # Normal version
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         if len(s)==0:
#             return None
#         length = len(s)-1
#         for i in range(len(s)//2):
#             tmp=s[i]
#             s[i]=s[length-i]
#             s[length-i]=tmp

#Pythonic Version:
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()