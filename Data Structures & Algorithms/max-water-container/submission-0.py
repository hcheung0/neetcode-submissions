class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l, r = 0, len(heights)-1
        largest_area = 0;

        while r > l:
            area = (r - l) * min(heights[r], heights[l])
            if area > largest_area:
                largest_area = area
            if heights[r] <= heights[l]:
                r -= 1
            elif heights[r] > heights[l]:
                l += 1


        return largest_area




        