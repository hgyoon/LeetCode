class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # first let's sort the numbers
        sorted_nums = sorted(nums)
        # from the smallest, we can invert that number and find two numbers which adds the three upto 0
        # we're using set to prevent duplicates (by hash!)
        output = set()
        for i in range(len(sorted_nums)):
            neg = sorted_nums[i] * -1
            # define start and end point
            start = i + 1
            end = len(sorted_nums) - 1 # - 1 cuz 0 indexing
            while (start < end):
                if sorted_nums[start] + sorted_nums[end] < neg:
                    start += 1
                elif sorted_nums[start] + sorted_nums[end] > neg:
                    end -= 1
                # if solution is found, append it to the output and increment/decrement the pointers cuz we don't need them anymore(the set must not contain duplicate triplets)
                else:
                    output.add((sorted_nums[i], sorted_nums[start], sorted_nums[end]))
                    start += 1
                    end -= 1
        return output
