class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums) # length of list

        # Create 3 arrays with length n
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        # Nothing to the left of index 0, nothing to the right of last index
        pref[0] = suff[n - 1] = 1 

        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]

        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        
        for i in range(n):
            res[i] = pref[i] * suff[i]
        
        return res

        
            