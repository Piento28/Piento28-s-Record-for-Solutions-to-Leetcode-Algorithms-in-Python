# Sort
# Time: O(nlogn)
# Space: O(n)
class Solution:
    def twoSum(self, nums, target):
        def SortKey(a):
            return a[0]
        nums = [[value,index] for index,value in enumerate(nums)]
        index_begin, index_end = 0,len(nums)-1
        nums.sort(key=SortKey)
        while (index_begin<index_end):
            tmp = nums[index_begin][0]+nums[index_end][0]
            if tmp == target:
                break;
            elif tmp<target:
                index_begin+=1
            else:
                index_end-=1
        return [nums[index_begin][1],nums[index_end][1]]

# Hash
# Time: O(n)
# Space: O(n)
class Solution:
    def twoSum(self, nums, target):
        bucket={}
        for i,v in enumerate(nums):
            tmp=target-v
            if bucket.get(tmp)!=None:
                return [bucket.get(tmp),i]
            bucket[v]=i