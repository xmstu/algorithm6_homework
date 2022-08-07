# -*- coding:utf-8 -*-
from typing import List
from heapq import heappush, heappop


class Pair:

    def __init__(self, value, index) -> None:
        self.value = value
        self.index = index
    
    def __lt__(self, other):
        return True if self.value > other.value else False

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        pq = []
        for i in range(len(nums)):
            heappush(pq, Pair(nums[i], i))
            if i >= k - 1:
                while pq[0].index <= i - k:
                    heappop(pq)
                ans.append(pq[0].value)
        
        return ans


class TestMaxSlidingWindow:

    """
    pytest -s 239_sliding_window_maximum.py::TestMaxSlidingWindow
    """

    def test(self):
        solution = Solution()

        nums = [1,3,-1,-3,5,3,6,7]
        k = 3
        assert [3,3,5,5,6,7] == solution.maxSlidingWindow(nums, k)

        nums = [1] 
        k = 1
        assert [1] == solution.maxSlidingWindow(nums, k)
