class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        d = {}
        for index, value in enumerate(nums):
            d[value] = index
        
        print(d)
        if target in d:
            return d[target]
        else:
            return -1