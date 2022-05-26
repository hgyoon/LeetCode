class Solution:
    def maxArea(self, height: List[int]) -> int:
        # we're going to make pointers on each end
        start = 0
        end = len(height) - 1
        largest_area = 0
        # iterate until the pointers meet
        while start < end:
            h_start = height[start]
            h_end = height[end]
            # find area by multiplying the diff of two pointers
            # and the minimum height between the two
            area = (end - start) * min(h_start, h_end)
            # save the maximum area
            largest_area = max(largest_area, area)
            # move the pointer to find the next largest (brute force)
            if h_start < h_end:
                # decrement end pointer to find the highest from the right
                start += 1
            else:
                # increment start pointer to find the highest from the left
                end -= 1
        return largest_area
