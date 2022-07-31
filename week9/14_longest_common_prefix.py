# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    编写一个函数来查找字符串数组中的最长公共前缀。
    如果不存在公共前缀，返回空字符串 ""。
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        纵向扫描, 将字符串数组当成一个矩阵进行扫描, 遇到同一列的字符不全等的就停止, 返回最长公共前缀
        """
        if not strs:
            return ""
        
        ncol, nrow = len(strs[0]), len(strs)
        for col in range(ncol):
            # 获取 第一行 第 col 列字符
            char = strs[0][col]
            # 该 char 与 剩下的对应的行列字符进行对比, 如果 col 已经等于某一个字符的长度, 就说明找到最长公共前缀, 或某一行的对应列字符与 char 不等, 也找到了最长公共前缀
            if any(col == len(strs[row]) or strs[row][col] != char for row in range(1, nrow)):
                return strs[0][:col]
        
        return strs[0]


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        分治法, 将求最长公共前缀转化为一个个小问题, 然后再合并
        """
        def isCommonPrefix(length):
            str0, count = strs[0][:length], len(strs)
            return all(strs[i][:length] == str0 for i in range(1, count))

        if not strs:
            return ""

        minLength = min(len(s) for s in strs)
        low, high = 0, minLength
        while low < high:
            mid = (high - low + 1) // 2 + low
            if isCommonPrefix(mid):
                low = mid
            else:
                high = mid - 1

        return strs[0][:low]


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        二分答案求解
        """
        def isCommonPrefix(length):
            str0, count = strs[0][:length], len(strs)
            return all(strs[i][:length] == str0 for i in range(1, count))

        if not strs:
            return ""

        minLength = min(len(s) for s in strs)
        low, high = 0, minLength
        while low < high:
            mid = (high - low + 1) // 2 + low
            if isCommonPrefix(mid):
                low = mid
            else:
                high = mid - 1

        return strs[0][:low]


class TestLongestCommonPrefix:

    """
    pytest -s 14_longest_common_prefix.py::TestLongestCommonPrefix
    """

    def test(self):
        solution = Solution()

        strs = ["flower","flow","flight"]
        assert "fl" == solution.longestCommonPrefix(strs)

        strs = ["dog","racecar","car"]
        assert "" == solution.longestCommonPrefix(strs)
