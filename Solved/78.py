class Solution:
    def subsets(self, nums):
        size = len(nums)
        a=0
        up_bound = 2**size
        answer=[]
        while a<up_bound:
            bit = bin(a)
            tmp=[]
            for i in range(2,len(bit)):
                if bit[i]=='1':
                    tmp.append(nums[len(bit)-i-1])
            answer.append(tmp)
            a+=1
        return answer