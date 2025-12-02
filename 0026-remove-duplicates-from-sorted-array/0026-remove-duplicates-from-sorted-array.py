class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 如果是空陣列，直接回傳 0
        if not nums:
            return 0
        
        # k 代表「下一個不重複數字要寫入的位置」
        k = 1
        
        # 讓 i 從第 1 個位置開始往後跑 (因為我們要跟前一個 i-1 比)
        for i in range(1, len(nums)):
            
            # 邏輯核心：
            # 如果「現在這個數字」跟「前一個數字」 不一樣
            if nums[i] != nums[i-1]:
                
                # 代表它是新的！把它抄寫到 k 的位置
                nums[k] = nums[i]
                
                # k 往後移一格，準備接下一個
                k += 1
        
        # 回傳 k (不重複數字的總數)
        return k