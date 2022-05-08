class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            number_index=abs(nums[i])
            nums[number_index]*=-1
            if nums[number_index] > 0:
                return number_index
        
