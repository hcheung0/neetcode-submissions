class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Use a hashmap {integer, frequency of each integer}
        # This might be brute-force
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        sorted_desc = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        frequent = dict(list(sorted_desc.items())[:k])

        return list(frequent.keys())
        
