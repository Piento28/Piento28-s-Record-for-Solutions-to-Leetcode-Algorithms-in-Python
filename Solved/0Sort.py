import time
import random
import heapq

class Solution:
    saved = []
    def Swap(self,a,b):
        return b,a
    def MergeSort_Operation(self,la,lb):
        saved=[0]*(len(la)+len(lb))
        i=0;j=0;k=0;
        while i<len(la) and j<len(lb):
            if la[i]<=lb[j]:
                saved[k] = la[i]
                k+=1
                i+=1
            else:
                saved[k] = lb[j]
                k+=1
                j+=1
        while i<len(la):
            saved[k]=la[i]
            k+=1
            i+=1
        while j<len(lb):
            saved[k]=lb[j]
            k+=1
            j+=1
        return saved

    def InsertionSort(self,lis):
        for i in range(len(lis)):
            for j in range(i-1,-1,-1):
                if lis[j+1]<lis[j]:
                    lis[j+1],lis[j]=self.Swap(lis[j+1],lis[j])
        return lis
    def BubbleSort(self,lis):
        for i in range(len(lis)-1):
            for j in range(i+1,len(lis)):
                if lis[i]>lis[j]:
                    lis[i],lis[j]=self.Swap(lis[i],lis[j])
        return lis
    def MergeSort(self,lis):
        if len(lis)==1:
            return lis
        else:
            return self.MergeSort_Operation(self.MergeSort(lis[:len(lis)//2]),self.MergeSort(lis[len(lis)//2:]))
    
#     def QuickSort(self,lis):
#         if len(lis)<=1:
#             return None
#         mid=random.randint(0,len(lis)-1)
#         i=0;j=len(lis)-1
#         print(mid,i,j)
#         while i<j:
#             print(mid,i,j)
#             while i<mid:
#                 print(mid,i,j)
#                 if lis[i]>lis[mid]:
#                     lis[i],lis[mid]=self.Swap(lis[i],lis[mid])
#                     mid=i
#                 i+=1
#             print('haha')
#             while j>mid:
#                 print(mid,i,j)
#                 if lis[j]<lis[mid]:
#                     lis[j],lis[mid]=self.Swap(lis[j],lis[mid])
#                     mid=j
#                 j-=1
#         print("hehe")
#         self.QuickSort(lis[:mid])
#         self.QuickSort(lis[mid:])
#         return lis
    def QuickSort(self,lis,start,end):
        if end-start<=0:
            return None
        mid=random.randint(start,end)
        i=start;j=end
        while i<j:
            while i<mid:
                if lis[i]>lis[mid]:
                    lis[i],lis[mid]=self.Swap(lis[i],lis[mid])
                    mid=i
                i+=1
            while j>mid:
                if lis[j]<lis[mid]:
                    lis[j],lis[mid]=self.Swap(lis[j],lis[mid])
                    mid=j
                j-=1
        self.QuickSort(lis,start,mid-1)
        self.QuickSort(lis,mid+1,end)
        return lis

test = Solution()
a = [3,4,5,6,1,2,7,0,-1,14,-6]
print(test.BubbleSort(a))
a = [3,4,5,6,1,2,7,0,-1,14,-6]
print(test.InsertionSort(a))
a = [3,4,5,6,1,2,7,0,-1,14,-6]
print(test.MergeSort(a))
a = [3,4,5,6,1,2,7,0,-1,14,-6]
print(test.QuickSort(a,0,len(a)-1))

size = 10000
low_bound = -1000
up_bound = 1000
a=[0]*size
for i in range(size):
    a[i]=random.randint(low_bound,up_bound)
# print("Waiting sorted lists: ",a)
time_start = time.process_time()
bubble = test.BubbleSort(a)
time_end = time.process_time()
print("Bubble Sort used time:%fs"%(time_end-time_start))
# print(bubble)

time_start = time.process_time()
# insertion = test.InsertionSort(a)
time_end = time.process_time()
print("Insertion Sort used time:%fs"%(time_end-time_start))
# print(insertion)

time_start = time.process_time()
merge = test.MergeSort(a)
time_end = time.process_time()
print("Merge Sort used time:%fs"%(time_end-time_start))
# print(merge)

time_start = time.process_time()
merge = test.QuickSort(a,0,len(a)-1)
time_end = time.process_time()
print("Quick Sort used time:%fs"%(time_end-time_start))
# print(merge)
