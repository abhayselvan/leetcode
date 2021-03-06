class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            
            index = abs(nums[i]) - 1
            
            if nums[index] > 0:
                nums[index] *= -1
                
        return [index + 1 for index, num in enumerate(nums) if num > 0]