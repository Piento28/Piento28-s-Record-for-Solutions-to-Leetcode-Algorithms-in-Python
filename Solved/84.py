class Solution:
    def largestRectangleArea(self, heights):
        if not heights:
            return 0
        heights.append(0)
        stack = []
        count_max = 0
        i = 0
        while i<len(heights):
            if (not stack) or heights[stack[-1]]<=heights[i]:
                stack.append(i)
                i+=1
            else:
                index = stack.pop(-1)
                if not stack:
                    length=i
                else:
                    length=i-stack[-1]-1
                count_max = max(count_max,heights[index]*length)
        return count_max