# time complexity: O(M+N)
# space complexity: O(1)


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ns1 = version1.split('.')
        ns2 = version2.split('.')

        for i in range(max(len(ns1), len(ns2))):
            v1 = int(ns1[i]) if i < len(ns1) else 0
            v2 = int(ns2[i]) if i < len(ns2) else 0
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
        return 0
