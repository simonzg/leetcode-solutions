class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda (h,k): (-h,k))
        q = []
        for [h,k] in people:
            q.insert(k, [h,k])
        return q
