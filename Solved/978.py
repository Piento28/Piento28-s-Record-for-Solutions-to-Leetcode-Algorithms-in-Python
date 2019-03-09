class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        updown = []
        
        if len(A)<=1:
            return len(A)
        for i in range(len(A)-1):
            if A[i]>A[i+1]:
                signed=1
            elif A[i]<A[i+1]:
                signed=-1
            else:
                signed=0
            updown.extend([signed])
        longest=[0]*len(updown)
        if updown[0]==0:
            longest[0]=0
        else:
            longest[0]=1
        for i in range(1,len(updown)):
            if updown[i]==0:
                longest[i]=0
            elif updown[i-1]*updown[i]==-1:
                longest[i]=longest[i-1]+1
            else:
                longest[i]=1
        how_max = 0
        for i in range(len(longest)):
            if longest[i]>how_max:
                how_max=longest[i]
        return how_max+1