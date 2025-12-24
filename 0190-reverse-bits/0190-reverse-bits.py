class Solution:
    def reverseBits(self, n: int) -> int:
        new_n = bin(n)[2:]
        new_fill_n = new_n.zfill(32)
        final_n = new_fill_n[::-1]
        return int(final_n,2)