class Codec:
    def __init__(self):
        self.map = {}
        
    def get_key(self):
        key = ''
        for i in range(6):
            d = random.randint(0, 35)
            if 0<=d<=9:
                key+=str(d)
            else:
                key+=chr(d)
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        key = self.get_key()
        while key in self.map:
            key = self.get_key()
        self.map[key] = longUrl
            

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        key = shortUrl
        if key in self.map:
            return self.map[key]
        return ''

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
