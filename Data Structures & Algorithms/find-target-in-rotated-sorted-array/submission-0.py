class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        d = {value: index for index, value in enumerate(nums)}
        
        print(d)
        if target in d:
            return d[target]
        else:
            return -1