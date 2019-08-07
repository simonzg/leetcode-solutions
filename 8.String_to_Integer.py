# regex
# time complexity: ?
# space complexity: ?


class Solution:
    def myAtoi(self, str: str) -> int:
        p = re.compile(r"([+-]?\d+)\D?")
        m = p.match(str.strip(' '))
        if m:
            val = int(m.group(1))
            if val > 2147483647:
                return 2147483647
            if val < -2147483648:
                return -2147483648
            return val
        else:
            return 0
