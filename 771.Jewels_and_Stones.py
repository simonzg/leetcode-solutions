class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        print([S.count(j) for j in J])
        return sum([S.count(j) for j in J])
