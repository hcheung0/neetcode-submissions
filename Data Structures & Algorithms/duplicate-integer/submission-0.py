class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = []

        for i, num in enumerate(nums):
            if num in d:
                return True
            d.append(num)
        
        return False