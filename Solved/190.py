class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        a=bin(n)
        a=list(a)
        a.reverse()
        a=a[:-2]
        a.extend(['0']*(32-len(a)))
        a=''.join(a)
        a=int(a,2)
        return a