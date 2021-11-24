class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l_min, l_max = 0, len(nums) - 1
        
        while l_max >= l_min:
            l_mid = l_min + (l_max - l_min)//2
            
            if target > nums[l_mid]:
                l_min = l_mid + 1
            elif target < nums[l_mid]:
                l_max = l_mid - 1 
            else:
                return l_mid
        return -1