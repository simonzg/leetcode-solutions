class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        
        l,r = 0, n-1
        water = 0
        minHeight = 0
        
        while l<r:
            while l<r and height[l] <= minHeight:
                water += minHeight - height[l]
                l+=1
            while l<r and height[r] <= minHeight:
                water += minHeight - height[r]
                r-=1
            minHeight = min(height[l], height[r])
        return water
