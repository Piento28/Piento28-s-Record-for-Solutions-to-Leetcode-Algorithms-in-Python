# # heapq.nlargest, corrent but TLE
# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         self.k = k
#         self.heap=nums
#         self.size=len(self.heap)
#     def add(self, val: int) -> int:
#         self.heap.append(val)
#         if self.k<=len(self.heap):
#             return heapq.nlargest(self.k,self.heap)[-1]


# # Handmade Smallest Heap
# class KthLargest:

#     def Swap(self,a,b):
#         tmp=a
#         a=b
#         b=tmp
#         return a,b
#     def shift_down(self,heap):
#         i=0
#         t=0
#         flag=True
#         while i*2+1<len(heap) and flag:
#             flag=False
#             if heap[i]>heap[i*2+1]:
#                 flag=True
#                 t=i*2+1
#                 if t+1<len(heap) and heap[t]>heap[t+1]:
#                     t=t+1
#             elif i*2+2<len(heap) and heap[i]>heap[i*2+2]:
#                 flag=True
#                 t=i*2+2
#             if flag:
#                 heap[i],heap[t]=self.Swap(heap[i],heap[t])
#                 i=t
#     def shift_up(self,i,heap):
#         i-=1
#         while i!=0 and heap[i]<heap[(i-1)//2]:
#             heap[i],heap[(i-1)//2]=self.Swap(heap[i],heap[(i-1)//2])
#             i=(i-1)//2
    
#     def __init__(self, k: int, nums: List[int]):
#         self.size = k
#         self.nums= []
#         self.heapsize=0
#         for i in range(len(nums)):
#             if self.heapsize<self.size:
#                 self.heapsize+=1
#                 self.nums.append(nums[i])
#                 self.shift_up(len(self.nums),self.nums)
#             else:
#                 if nums[i]>self.nums[0]:
#                     self.nums[0]=nums[i]
#                     self.shift_down(self.nums)

#     def add(self, val: int) -> int:
#         if len(self.nums)<self.size:
#             self.nums.append(val)
#             self.shift_up(len(self.nums),self.nums)
#             if len(self.nums)==self.size:
#                 return self.nums[0]
#         else:
#             if val<=self.nums[0]:
#                 return self.nums[0]
#             else:
#                 self.nums[0]=val
#                 self.shift_down(self.nums)
#                 return self.nums[0]


# Python3 import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap=[]
        self.k=k
        heapq.heapify(self.heap)
        for i in range(len(nums)):
            if len(self.heap)<self.k:
                heapq.heappush(self.heap, nums[i])
            elif nums[i]>self.heap[0]:
                heapq.heapreplace(self.heap,nums[i])

    def add(self, val: int) -> int:
        if len(self.heap)<self.k:
            heapq.heappush(self.heap,val)
            if len(self.heap)==self.k:
                return self.heap[0]
        else:
            if val<=self.heap[0]:
                return self.heap[0]
            else:
                heapq.heapreplace(self.heap,val)
                return self.heap[0]