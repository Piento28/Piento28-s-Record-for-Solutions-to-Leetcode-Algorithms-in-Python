# KMP Version, but slower....
class Solution:
    def get_next(self,a):
        k=-1
        i=0
        link=[-1]*(len(a)+1)
        while i<len(a):
            if (k==-1 or a[i]==a[k]):
                i+=1
                k+=1
# out in index problem, need fiexed optimisation
#                 if a[i]==a[k]:
#                     link[i]=link[k]
#                 else:
#                     link[i]=k
                link[i]=k
            else:
                k=link[k]
        return link
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        link = self.get_next(list(needle))
        i=0;j=0;
        while i<len(haystack):
            while i<len(haystack) and haystack[i]==needle[j]:
                i+=1
                j+=1
                if j==len(needle):
                    return i-len(needle)
            if link[j]==-1:
                i+=1
                j=0
            else:
                j=link[j]
        return -1
# # Normal version
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if len(needle)==0:
#             return 0
#         else:
#             l=len(needle)
#             for i in range(len(haystack)):
#                 if(haystack[i:i+l]==needle):
#                     return i
#         return -1