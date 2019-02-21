class Solution(object):
    def maxArea(self, height):
        j = len(height)-1
        i = 0
        w = []
        while i < j:
            if height[i] > height[j]:
                w.append(height[j]*(j-i))
                j=j-1
            if height [i] <= height[j]:
                
                w.append(height[i]*(j-i))
                i = i+1
                
        w.sort()
        return w[-1]
