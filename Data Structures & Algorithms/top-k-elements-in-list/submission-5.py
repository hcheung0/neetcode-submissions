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
        
        # Use bucket sort
        # Essentially, the "bucket" is an array where the indexes = the frequency or count
        # of each integer
        # The length is len(nums) + 1 since a frequency of 0 is redundant
            # Correction* it's so index len(nums) exists

        # buckets = [[]] * (len(nums)+1) (this is incorrect b/c it makes n reference
        # to the same list)
        buckets = [[] for n in range(len(nums)+1)]
        for num, freq in d.items():
            buckets[freq].append(num)
        
        top_k = []
        for bucket in reversed(buckets):
            if len(top_k) == k:
                return top_k
            top_k.extend(bucket)

        
        
        # we want to start at the end of buckets and count down until we reach k items.
        # dont forget about repeating frequencies


        
