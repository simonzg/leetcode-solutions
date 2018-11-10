class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        convert_map = {'2':'abc', '3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res = []
        for d in digits:
            chs = convert_map[d]
            if not res:
                res = list(chs)
            else:
                res = [ s+ch for ch in chs for s in res ]
        return res
