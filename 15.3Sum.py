# Loop over the array to degrade the problem to twoSum
# time complexity: O(N) for loop, O(logN) for twoSum, so total O(N*logN)
# space complexity: O(N)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)

        def twoSum(i, target):
            ans = []
            l, r = i, n-1
            while l < r:
                lv, lr = nums[l], nums[r]
                s = lv + lr
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    ans.append([nums[l], nums[r]])
                    while l < r and nums[l] == lv:
                        l += 1
                    while l < r and nums[r] == lr:
                        r -= 1
            return ans
        i = 0
        ans = []
        while i < n-2:
            v = nums[i]
            for item in twoSum(i+1, -nums[i]):
                ans.append([v]+item)

            while i < n-2 and nums[i] == v:
                i += 1

        return ans
