# -*- coding:utf-8 -*-
from collections import defaultdict


class Solution:
    """
    给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1 
    """
    def firstUniqChar(self, s: str) -> int:
        # 构建字符统计 map
        char_map = defaultdict(int)
        for char in s:
            char_map[char] += 1
        for index, char in enumerate(s):
            if char_map[char] == 1:
                return index
        
        return -1


class TestFirstUniqChar:
    """
    pytest -s 387_first_unique_character_in_str.py::TestFirstUniqChar
    """

    def test(self):

        solution = Solution()

        s = "leetcode"
        assert 0 == solution.firstUniqChar(s)

        s = "loveleetcode"
        assert 2 == solution.firstUniqChar(s)

        s = "aabb"
        assert -1 == solution.firstUniqChar(s)
