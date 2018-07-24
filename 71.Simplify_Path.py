class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        paths = path.split('/')
        for p in paths:
            if p == '..':
                if stack:
                    stack.pop()
            elif p != '.' and p != '':
                stack.append(p)
        if not stack:
            return '/'
        return '/'+'/'.join(stack)
        
        
