class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # 這負責寫入好數字的位置
        
        # i開始檢查
        for i in range(len(nums)):
            
            # 如果發現不是 val
            if nums[i] != val:
                # 把它抄寫到 k 的位置
                nums[k] = nums[i]
                # k 往後移一格，準備接下一個好數字
                k += 1
        
        # 迴圈跑完，前 k 個就是乾淨的陣列
        return k