class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        L = list(s)
        i,j = 0,len(L)-1
        while i<j:
            while i<j and L[i] not in vowels:
                i += 1
            while i<j and L[j] not in vowels:
                j -= 1
            L[i],L[j] = L[j], L[i]
            i += 1
            j -= 1
            
        return ''.join(L)
