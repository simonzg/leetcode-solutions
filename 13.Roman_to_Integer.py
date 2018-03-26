class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        target = s
        trans = {
            "CM": 900,
            "CD": 400,
            "XC": 90,
            "XL": 40,
            "IX": 9,
            "IV": 4,
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }
        print(trans.keys())
        while (target):
            for ch in trans.keys():
                if target.startswith(ch):
                    num += trans[ch]
                    target = target[len(ch):]
                    break
        return num

if __name__=="__main__":
    r = Solution().romanToInt("DCXXI")
    print(r)
