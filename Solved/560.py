class Solution:
    def subarraySum(self, nums, k):
        dic={}
        dic[0]=1
        cum_sum=0
        answer=0
        for i in range(len(nums)):
            cum_sum+=nums[i]
            tmp=cum_sum-k
            if (tmp in dic):
                answer+=dic[tmp]
            if cum_sum in dic:
                dic[cum_sum]+=1
            else:
                dic[cum_sum]=1
        return answer