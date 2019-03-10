class Solution:
    def BinarySearch(self, a, i,j,target):
        while i<j:
            mid = (i+j)//2
            if a[mid]>target:
                j=mid
            elif a[mid]<target:
                i=mid+1
            elif a[mid]==target:
                return mid
        return j
    def lengthOfLIS(self, nums) -> int:
        if not nums:
            return 0
        tail = [0 for i in range(len(nums)+1)]
        tail[1] = nums[0]
        size = 1
        for i in range(1,len(nums)):
            if nums[i]>tail[size]:
                size+=1
                tail[size]=nums[i]
            elif nums[i]<tail[size]:
                insert = self.BinarySearch(tail,1,size,nums[i])
                tail[insert]=nums[i]
        return size