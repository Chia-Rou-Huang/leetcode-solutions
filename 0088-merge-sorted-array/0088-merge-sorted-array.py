class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # p1 指向 nums1 有效數字的尾巴
        p1 = m - 1
        # p2 指向 nums2 的尾巴
        p2 = n - 1
        # p 指向 nums1 目前最尾端要填寫的位置
        p = m + n - 1
        
        # 當兩個陣列都還有數字的時候，開始比較
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1] # nums1 的比較大，填進去
                p1 -= 1              # p1 往前移
            else:
                nums1[p] = nums2[p2] # nums2 的比較大，填進去
                p2 -= 1              # p2 往前移
            p -= 1                   # 填寫位置往前移
            
        # 特殊情況：如果 nums2 還有剩 (例如 nums1 的數字都很大，先把位置填滿了)
        # 把 nums2 剩下的全部抄進去
        # (如果 nums1 有剩不用管，因為它們本來就在對的位置上)
        nums1[:p2+1] = nums2[:p2+1]