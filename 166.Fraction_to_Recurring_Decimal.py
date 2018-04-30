class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = '-' if (numerator>=0) ^ (denominator>=0) and numerator !=0 else ''
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        digit = numerator // denominator
        numerator %= denominator
        integer = str(digit)
        if numerator == 0:
            return sign + integer
        
        digit = 0
        fraction = "."
        table = {}
        i = 1
        while numerator:
            if numerator not in table:
                table[numerator] = i
            else:
                i = table[numerator]
                fraction = fraction[:i] + '(' + fraction[i:]+ ')'
                break
                   
            numerator *= 10
            digit = numerator // denominator
            fraction += str(digit)
            numerator %= denominator
            i += 1
            
        return sign + integer + fraction
