class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1=0
        p2=0
        dic = {}
        string = list(s)
        if len(string)<=1:
            return len(string)
        dic[string[0]]=0
        count_max=0
        while p2<len(string)-1:
            p2+=1
            if string[p2] in dic and dic[string[p2]]>=p1:
                p1=dic[string[p2]]+1
                dic[string[p2]]=p2
            else:
                dic[string[p2]]=p2
            count_max = max(count_max,p2-p1+1)
        return count_max