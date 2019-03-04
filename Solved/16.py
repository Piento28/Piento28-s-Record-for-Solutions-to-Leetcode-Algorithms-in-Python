#BinarySearch Version, slower:
# class Solution:
#     def binarysearch(self,nums,target):
#         if target>=nums[-1]:
#             return len(nums)-2
#         i,j=0,len(nums)-1
#         while j-i>=2:
#             mid = (j+i)//2
#             if target<nums[mid]:
#                 j=mid
#             elif target>nums[mid]:
#                 i=mid
#             elif target == nums[mid]:
#                 i=j=mid
#                 return i
#         return i
#     def threeSumClosest(self, nums, target):
#         nums.sort()
#         all_len = len(nums)
#         cloest_sum = 2147483647
#         ssum = 0
#         for i in range(all_len-2):
#             for j in range(i+1,all_len-1):
#                 aim = target-nums[i]-nums[j]
#                 pro_nums = nums.copy()
#                 del(pro_nums[j])
#                 del(pro_nums[i])
#                 left = self.binarysearch(pro_nums,aim)
#                 if abs(aim-pro_nums[left])<cloest_sum:
#                     cloest_sum = abs(aim-pro_nums[left])
#                     ssum = nums[i] + nums[j] + pro_nums[left]
#                 if (left+1<(all_len-2)) and abs(aim-pro_nums[left+1])<cloest_sum:
#                     cloest_sum = abs(aim-pro_nums[left+1])
#                     ssum = nums[i] + nums[j] + pro_nums[left+1]
#                 if cloest_sum==0:
#                     return ssum
#         return ssum
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j, k = i+1, len(nums) - 1
            while j < k:
                tmp = nums[i] + nums[j] + nums[k]
                if tmp == target:
                    return tmp
                if abs(tmp - target) < abs(result - target):
                    result = tmp
                if tmp < target:
                    j += 1
                elif tmp > target:
                    k -= 1
        return result