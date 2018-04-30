class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        if n == 0:
            return 0
        n_bits = 32
        bits = [(n>>bit)&1 for bit in range(0, n_bits)]
        i = 1
        n = bits[0]
        while i < n_bits:
            n = (n<<1) + bits[i]
            i+=1
        return n
        
        
