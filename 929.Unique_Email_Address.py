class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        uniques = set([])
        for email in emails:
            prefix, domain = email.split('@')
            prefix = prefix.split('+')[0]
            prefix = prefix.replace('.','')
            unique = prefix + '@' + domain
            uniques.add(unique)
        return len(uniques)