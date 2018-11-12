class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        sum_ud = sum_lr = 0
        for ch in moves:
            if ch == 'U':
                sum_ud += -1
            if ch == 'D':
                sum_ud += 1
            if ch == 'L':
                sum_lr += -1
            if ch == 'R':
                sum_lr += 1
        return sum_lr == 0 and sum_ud == 0
