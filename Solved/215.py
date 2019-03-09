class Solution:

    def Swap(self,a,b):
        tmp=a
        a=b
        b=tmp
        return a,b
    def shift_down(self,heap):
        i=0
        t=0
        flag=True
        while i*2+1<len(heap) and flag:
            flag=False
            if heap[i]>heap[i*2+1]:
                flag=True
                t=i*2+1
                if t+1<len(heap) and heap[t]>heap[t+1]:
                    t=t+1
            elif i*2+2<len(heap) and heap[i]>heap[i*2+2]:
                flag=True
                t=i*2+2
            if flag:
                heap[i],heap[t]=self.Swap(heap[i],heap[t])
                i=t
    def shift_up(self,i,heap):
        i-=1
        while i!=0 and heap[i]<heap[(i-1)//2]:
            heap[i],heap[(i-1)//2]=self.Swap(heap[i],heap[(i-1)//2])
            i=(i-1)//2
    
    def findKthLargest(self, nums, k):
        self.size = k
        self.nums= []
        self.heapsize=0
        for i in range(len(nums)):
            if self.heapsize<self.size:
                self.heapsize+=1
                self.nums.append(nums[i])
                self.shift_up(len(self.nums),self.nums)
            else:
                if nums[i]>self.nums[0]:
                    self.nums[0]=nums[i]
                    self.shift_down(self.nums)
        return self.nums[0]