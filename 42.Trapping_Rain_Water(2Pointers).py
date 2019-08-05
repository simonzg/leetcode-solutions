'''
Two pointers

This could also be solved by DP
'''
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        water = 0
        while l<r:
            level = min(height[l], height[r])
            if height[l] < height[r]:
                while height[l] <= level and l<r:
                    water += level - height[l]
                    l+=1
            else:
                while height[r] <= level and l<r:
                    water += level - height[r]
                    r-=1
        return water
