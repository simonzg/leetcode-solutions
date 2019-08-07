# divide and conquer matrix => arrays
# time complexity: O(N*logN)
# space complexity: O(1)


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def search(row, target):
            l, r = 0, len(row)-1
            while l < r:
                mid = (l+r)//2 + 1
                if row[mid] > target:
                    r = mid-1
                elif row[mid] < target:
                    l = mid+1
                else:
                    return True
            return row[l] == target

        if not matrix or not matrix[0]:
            return False

        for row in matrix:
            if row[0] <= target and row[-1] >= target:
                if search(row, target):
                    return True
        return False
