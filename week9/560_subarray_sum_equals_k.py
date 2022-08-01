# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的连续子数组的个数 。
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 构建前缀和数组
        n = len(nums)
        preSum = [0] * (n + 1)

        for index in range(0, n):
            preSum[index + 1] = preSum[index] + nums[index]
        
        print(f"preSum: {preSum}")
        # 区间和 [left..right]，注意下标偏移
        ans = 0
        for left in range(0, n):
            for right in range(left, n):
                print(f"fuck left: {left}, right: {right}, right+1: {right+1}")
                if preSum[right+1] - preSum[left] == k:
                    ans += 1
        return ans        


class Solution2:
    """
    给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的连续子数组的个数 。
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        利用字典记录前缀和的出现次数
        """
        # key: 前缀和, value: 对应的出现次数
        pre_sum_map = {0:1}

        pre_sum = 0
        count = 0

        # 遍历所有元素: 计算前缀和, 寻找 k, 更新map
        for num in nums:
            # 累计前缀和
            pre_sum += num

            # 根据 pre - (pre - k) = k，寻找连续数组为 pre - k 的数量，即连续数组的和为 k 的数量
            # 说明：pre 为自首个元素开始累计的连续数组；
            # pre - k 为包含在连续数组 pre 中的一个连续子数组（自首个元素开始累计）
            # 连续数组 - 连续子数组 = 连续子数组，对应 pre - (pre - k) = k
            # 则连续数组的和为 pre - k 的数量，即为连续数组的和为 k 的数量
            if pre_sum - k in pre_sum_map:
                count += pre_sum_map[pre_sum - k]

            if pre_sum in pre_sum_map:
                pre_sum_map[pre_sum] += 1
            else:
                pre_sum_map[pre_sum] = 1
        
        return count


class TestSubarraySum:

    """
    pytest -s 560_subarray_sum_equals_k.py::TestSubarraySum
    """

    def test(self):
        solution = Solution2()

        nums = [1,1,1]; k = 2
        assert 2 == solution.subarraySum(nums, k)

        nums = [1,2,3]; k = 3
        assert 2 == solution.subarraySum(nums, k)

        nums = [-1,-1,1]; k = 0
        assert 1 == solution.subarraySum(nums, k)
