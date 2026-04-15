class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        # a 代表前前一步 (n-2)，b 代表前一步 (n-1)
        a, b = 1, 2
        
        # 從第 3 階開始算到第 n 階
        for i in range(3, n + 1):
            current = a + b # 當前這一階 = 前兩階相加
            a = b           # 更新：原本的前一步變成前前一步
            b = current     # 更新：原本的當前階變成前一步
            
        return b