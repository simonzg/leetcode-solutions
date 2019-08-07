# partition with random pivot
# time complexity: O(N) in average cases, O(N^2) in worst cases
# space complexity: O(1)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # select the K-largest from nums[i:j]
        def select(i, j, K):
            if i == j:
                return nums[i]

            idx = random.randint(i, j)

            nums[i], nums[idx] = nums[idx], nums[i]
            mid = partition(i, j)
            length = mid - i + 1
            if length > K:
                return select(i, mid, K)
            elif length < K:
                return select(mid+1, j, K-length)
            else:
                return nums[mid]

        # partition nums[i:j] with nums[i] as pivot
        def partition(i, j):
            pivot = nums[i]
            l = i+1
            r = j
            while True:
                while l < r and nums[l] > pivot:
                    l += 1
                while l <= r and nums[r] <= pivot:
                    r -= 1
                if l >= r:
                    break
                nums[l], nums[r] = nums[r], nums[l]
            nums[i], nums[r] = nums[r], nums[i]
            return r

        return select(0, n-1, k)
