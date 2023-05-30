from typing import List
from operator import itemgetter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use max k times
        # arr = [0 for a in range(20001)] 
        # ans = []
        # for i in nums:
        #     arr[i+10000] += 1
        # for j in range(k):
        #     b = arr.index(max(arr))
        #     ans.append(b-10000)
        #     arr[b] = 0
        # return(ans)


solo = Solution()
print(solo.topKFrequent(nums = [1,1,1,2,2,3], k = 1))