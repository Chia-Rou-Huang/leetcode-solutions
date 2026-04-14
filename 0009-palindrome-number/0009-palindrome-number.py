class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        
        if x >= 0:
            n=len(str(x))
            c= n//2
            m=str(x)
            for i in range(c+1):
                if m[i] != m[-i-1]:
                    return False
            return True
        