# permutation
# time complexity: O(3^N*4^M) where N is the number of digits that maps to 3 letters
# M is the number of digits that maps to 4 letters
# space complexity: O(3^N*4^M)


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums = "2,3,4,5,6,7,8,9".split(',')
        chs = "abc,def,ghi,jkl,mno,pqrs,tuv,wxyz".split(',')
        memo = dict(zip(nums, chs))

        ans = []
        for d in digits:
            if not ans:
                ans = memo[d]
            else:
                ans = [prefix+ch for ch in memo[d] for prefix in ans]

        return ans
