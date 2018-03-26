class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()
        numbers = set(nums[:])
        for i,v in enumerate(nums):
            newNums = nums[:]
            del newNums[i]
            combinations = self.findSum(newNums, 0-v)
            if len(combinations) > 0:
                for c in combinations:
                    c.insert(0,v)
                    c.sort()
                    if (not c in results):
                        results.append(c)
        return results
                
            
    def findSum(self, nums, targetSum):
        i = 0
        j = len(nums)-1
        results = []
        while (i<j):
            currentSum = nums[i]+nums[j]
            if currentSum == targetSum:
                results.append([nums[i], nums[j]])
                i += 1
            if currentSum < targetSum:
                i += 1
            if currentSum > targetSum:
                j -= 1
        return results

if __name__=="__main__":
    r = Solution().threeSum([-4, -2,0,2,4,6])
    print(r)
