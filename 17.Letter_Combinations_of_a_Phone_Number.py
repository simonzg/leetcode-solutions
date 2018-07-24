class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_map = dict(zip('2,3,4,5,6,7,8,9'.split(','), 'abc,def,ghi,jkl,mno,pqrs,tuv,wxyz'.split(',')))
        n = len(digits)
        if not digits:
            return []
        r = ['']
        
        for i in range(n):
            r = [ prefix + ch for prefix in r for ch in digit_map[digits[i]]]
        return r
