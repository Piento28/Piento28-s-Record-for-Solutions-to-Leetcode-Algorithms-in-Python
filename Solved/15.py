class Solution:
    def threeSum(self, nums):
        nums.sort()
        dic = {}
        answer=[]
        for x in nums:
            if dic.get(x):
                dic[x] += 1
            else:
                dic[x] = 1
        if (0 in dic) and (dic[0]>=3):
            answer.append([0,0,0])
        dic_list = list(dic)
        i,j=0,0
        all_len = len(dic_list)   
        while i<all_len and dic_list[i]<0:
            dic[dic_list[i]] -= 1
            j=i
            up_bound = abs(dic_list[i])//2
            while  j<all_len and dic_list[j]<=up_bound:
                complement = -dic_list[i]-dic_list[j]
                if complement == dic_list[j]:
                    if dic[complement]>=2:
                        answer.append([dic_list[i],complement,complement])
                elif dic[dic_list[j]]>=1 and (complement in dic) and dic[complement]>=1:
                        answer.append([dic_list[i],dic_list[j],complement])
                j += 1
            i += 1
        return answer