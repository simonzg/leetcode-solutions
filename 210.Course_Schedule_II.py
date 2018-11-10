'''
REF: https://leetcode.com/problems/course-schedule-ii/discuss/179845/Python-solution-similar-to-207.-Course-Schedule
'''
class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        deps = dict([(i, []) for i in range(numCourses)])
        visited = dict([(i, 0) for i in range(numCourses)])
        for c,p in prerequisites:
            deps[c].append(p)
        
        def dfs(i, tempStack):
            # return whether if the dependency has loop
            if visited[i] == 1:
                return False
            if visited[i] == -1:
                return True
            visited[i] = 1
            
            for d in deps[i]:
                if not dfs(d, tempStack):
                    return False
            visited[i] = -1
            tempStack.append(i)
            return True
        
        res = []
        for i in range(numCourses):
            tempStack = []
            if not dfs(i, tempStack):
                return []
            res += tempStack
        return res
