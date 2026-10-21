class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d1 = {}
        for i, num in enumerate(nums):
            if target - num in d1:
                return [d1[target-num], i]
            else:
                d1[num] = i
        

            