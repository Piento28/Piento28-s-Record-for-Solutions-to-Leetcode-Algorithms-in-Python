# # DP
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         if len(s)<=1:
#             return 0
#         state = [0 for i in range(len(s)+1)]
#         s=list(s)
#         s.append('*')
#         count_max=0
#         for i in range(1,len(s)-1):
#             if s[i]==')':
#                 if s[i-1]=='(':
#                     state[i]=state[i-2]+2
#                     count_max = max(count_max,state[i])
#                 elif s[i-state[i-1]-1]=='(':
#                     state[i]=state[i-1]+2+state[i-state[i-1]-2]
#                     count_max = max(count_max,state[i])
#         return count_max

# Stack
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s)<=1:
            return 0
        s=list(s)
        stack=[-1]
        count_max=0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                stack.pop(-1)
                if not stack:
                    stack.append(i)
                else:
                    count_max=max(count_max,i-stack[-1])
        return count_max