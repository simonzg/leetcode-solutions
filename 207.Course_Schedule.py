class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preCount = {}
        followings = {}

        for i in range(numCourses):
            preCount[i] = 0  # key: courseID, value: count of prerequisites
            followings[i] = []  # key: courseID, value: [] of following courses

        for course, prereq in prerequisites:
            preCount[course] += 1
            followings[prereq].append(course)

        queue = []
        for course in preCount:
            count = preCount[course]
            if count == 0:
                queue.append(course)

        while queue:
            course = queue.pop(0)
            for fc in followings[course]:
                preCount[fc] -= 1
                if preCount[fc] == 0:
                    queue.append(fc)
            del(preCount[course])
        return not preCount
