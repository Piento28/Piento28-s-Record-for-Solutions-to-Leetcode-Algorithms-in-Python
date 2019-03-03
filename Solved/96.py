class Solution:
    def numTrees(self, n: int) -> int:
        s=[]
        s.extend([1,1])
        if n<=1:
            return s[0]
        for i in range(2,n+1):
            s.append(0)
            for j in range(1,i+1):
                s[i] += s[j-1]*s[i-j]
        return s[n]
            