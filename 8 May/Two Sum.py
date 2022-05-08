class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        for i, j in enumerate(nums):
            if j in dict1:
                return [dict1[j],i]
            dict1[target-j]=i
