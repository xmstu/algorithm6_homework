# -*- coding:utf-8 -*-
from typing import List


class Solution:

    """
    编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
    不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
    """
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


class TestReverseString:

    """
    pytest -s 344_reverse_string.py::TestReverseString
    """

    def test(self):
        solution = Solution()

        s = ["h","e","l","l","o"]
        solution.reverseString(s)
        assert ["o","l","l","e","h"] == s

        s = ["H","a","n","n","a","h"]
        solution.reverseString(s)
        assert ["h","a","n","n","a","H"] == s

    