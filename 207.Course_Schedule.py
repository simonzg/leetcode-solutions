class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        deps = dict([(i,[]) for i in range(numCourses)])
        visited = dict([(i,0) for i in range(numCourses)])
        
        for c,p in prerequisites:
            deps[c].append(p)
        
        def hasLoop(i):
            if visited[i] == 1:
                return True
            if visited[i] == -1:
                return False
            visited[i] = 1
            for d in deps[i]:
                if hasLoop(d):
                    return True
            visited[i] = -1
            return False
        
        for i in range(numCourses):
            if hasLoop(i):
                return False
        return True