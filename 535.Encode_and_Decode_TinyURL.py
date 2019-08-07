# two reversed maps


class Codec:
    def __init__(self):
        self.cache = {}
        self.reverse = {}

    def randomHex(self, n):
        chs = '0123456789abcdefghijklmnopqrstuvwxyz'
        ans = ''
        for i in range(n):
            ans += chs[random.randint(0, len(chs)-1)]
        return ans

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.reverse:
            return self.reverse[longUrl]
        randHex = self.randomHex(8)
        while randHex in self.cache:
            randHex = self.randomHex(8)
        self.cache[randHex] = longUrl
        url = 'http://tinyurl.com/'+randHex
        self.reverse[longUrl] = url
        return url

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        if not shortUrl:
            return ''
        randHex = shortUrl.replace('http://tinyurl.com/', '')
        if randHex in self.cache:
            return self.cache[randHex]
        return ''

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
