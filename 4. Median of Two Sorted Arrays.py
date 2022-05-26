class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # get the size of two arrays
        size_1 = len(nums1)
        size_2 = len(nums2)
        # initialize indexes for iteration
        index_1 = 0
        index_2 = 0
        # check if the length of array is even that it needs to be divided by 2
        even = 0
        # initialize a new array & index
        merged = []
        i = 0
        # see if the number is even
        if (size_1 + size_2) % 2 == 0:
            even = 1
        while True:
            n1 = nums1[index_1] if index_1 < size_1 else 1000001
            n2 = nums2[index_2] if index_2 < size_2 else 1000001
            if n1 < n2:
                merged.append(n1)
                index_1 += 1
            else:
                merged.append(n2)
                index_2 += 1
            # if i reached the middle point ex) 15 -> 7, 16 -> 8
            if i == (size_1 + size_2) // 2:
                # when there is odd number of elements, 3 // 2 -> 1 but we use 0 indexing so 1 is the middle
                if even == 0:
                    return merged[i]
                else:
                    return (merged[i-1] + merged[i]) / 2
            i += 1
        
