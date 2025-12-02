class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        
        for i in range(len(nums)):
            temp_index = nums[i] 
            val = nums[temp_index] 
            ans.append(val)
            
        return ans