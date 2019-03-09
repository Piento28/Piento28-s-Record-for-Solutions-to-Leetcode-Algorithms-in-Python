class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        lis=A
        for i in range(len(lis)):
            lis[i]=lis[i]**2
        lis.sort()
        return lis