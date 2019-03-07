class Solution:
    def dot(self,ma,mb):
        tmp=[[0,0],[0,0]]
        tmp[0][0]=ma[0][0]*mb[0][0]+ma[0][1]*mb[1][0]
        tmp[0][1]=ma[0][0]*mb[0][1]+ma[0][1]*mb[1][1]
        tmp[1][0]=ma[1][0]*mb[0][0]+ma[1][1]*mb[1][0]
        tmp[1][1]=ma[1][0]*mb[0][1]+ma[1][1]*mb[1][1]
        return tmp
    def get_mat(self, times):
        if times ==1:
            return [[1,1],[1,0]]
        if times ==2:
            return [[2,1],[1,1]]
        if times%2==0:
            return self.dot(self.get_mat(times//2),self.get_mat(times//2))
        else:
            return self.dot([[1,1],[1,0]],self.dot(self.get_mat(times//2),self.get_mat(times//2)))
    def fib(self, n):
        if n==0:
            return 0
        if n==1:
            return 1
        mat = [[0,0],[0,0]]
        mat = self.get_mat(n-1)
        return mat[0][0]

