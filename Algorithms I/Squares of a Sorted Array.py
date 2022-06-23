#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j, k = 0, len(nums) - 1, len(nums) - 1
        output = [None]*(j+1)
        while i <= j:
            if nums[i]**2 > nums[j]**2:
                output[k] = nums[i]**2
                i +=1 
            else:
                output[k] = nums[j]**2
                j -= 1
            k -= 1
            print(i, j, k)
            
        return output