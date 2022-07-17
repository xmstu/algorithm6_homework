# -*- coding:utf-8 -*-
from typing import List


class Solution:


    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0] * n
        for i in range(1, n):
            j = 0
            while j + nums[j] < i:
                j += 1
            dp[i] = dp[j] + 1
        return dp[n-1]


class TestJump:
    """
    pytest -s 45_jump_game_2.py::TestJump
    """

    def test(self):
        solution = Solution()

        nums = [2,3,1,1,4]
        assert 2 == solution.jump(nums)

        nums = [2,3,0,1,4]
        assert 2 == solution.jump(nums)