
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ns1 = version1.split('.')
        ns2 = version2.split('.')

        ns1 = [int(w) for w in ns1 if w]
        ns2 = [int(w) for w in ns2 if w]

        for i in range(max(len(ns1), len(ns2))):
            v1 = ns1[i] if i < len(ns1) else 0
            v2 = ns2[i] if i < len(ns2) else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0
