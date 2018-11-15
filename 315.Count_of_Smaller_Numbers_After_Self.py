class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def mergeSort(arr):
            half = len(arr)//2
            if half:
                left, right = mergeSort(arr[:half]), mergeSort(arr[half:])
                for i in range(len(arr))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        res[left[-1][0]] += len(right)
                        arr[i] = left.pop()
                    else:
                        arr[i] = right.pop()
            return arr
        res = [0 for i in range(len(nums))]
        mergeSort(list(enumerate(nums)))
        return res