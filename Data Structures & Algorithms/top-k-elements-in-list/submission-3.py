class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        sorted_d = dict(sorted(d.items(), key=lambda pair: pair[1], reverse=True))
        sorted_list = list(sorted_d.keys())[:k]

        return sorted_list

        # Sort the dictionary by value, from highest to lowest
        # Turn dictionary into a list of size k containing only the first k keys in the sorted order
        # Return the list
        
        
        