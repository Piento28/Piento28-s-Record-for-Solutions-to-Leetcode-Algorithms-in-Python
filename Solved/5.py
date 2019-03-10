# # Time O(n^2), Space O(n^2)
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s)<=1:
#             return s
#         s = list(s)
#         state = [[0 for i in range(len(s))] for i in range(len(s))]
#         count_max=1
#         count_i=0
#         count_j=0
#         for i in range(len(s)):
#             state[i][i]=1
#         for k in range(1,len(s)):
#             for i in range(len(s)-k):
#                 j=i+k
#                 if j-i==1:
#                     if s[i]==s[j]:
#                         state[i][j]=2
#                         if state[i][j]>count_max:
#                             count_max=state[i][j]
#                             count_i=i
#                             count_j=j
#                 else:
#                     if s[i]==s[j] and state[i+1][j-1]>0:
#                         state[i][j]=state[i+1][j-1]+2
#                         if state[i][j]>count_max:
#                             count_max=state[i][j]
#                             count_i=i
#                             count_j=j
#         return ''.join(s[count_i:count_j+1])

# Time O(n^2), Space O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        s = list(s)
        new_s = '*'.join(s)
        new_s = ["*"]+list(new_s)+["*"]
        count_max=0
        count_i=0
        count_j=0
        for i in range(len(new_s)):
            j=1
            current = 1
            while i-j>=0 and i+j<len(new_s):
                if new_s[i-j]==new_s[i+j]:
                    current += 2
                    if current>count_max:
                        count_max=current
                        count_i=i-j
                        count_j=i+j
                    j+=1
                else:
                    break
        if count_i%2==0:
            count_i+=1
            count_j-=1
            count_i//=2
            count_j//=2
        else:
            count_i//=2
            count_j//=2
        return ''.join(s[count_i:count_j+1])