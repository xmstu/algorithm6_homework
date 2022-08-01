# -*- coding:utf-8 -*-
from collections import defaultdict


class Solution:
    """
    给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
    注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
    """
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = defaultdict(int)
        for char in s:
            s_map[char] += 1
        
        for char in t:
            if s_map[char] == 0:
                return False
            s_map[char] -= 1
        
        for char in s:
            if s_map[char] != 0:
                return False
        
        return True


class Solution2:
    
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)

        s_list.sort()
        t_list.sort()
        return s_list == t_list


class Solution3:
    
    def isAnagram(self, s: str, t: str) -> bool:
        c1, c2 = [0] * 26, [0] * 26

        for char in s:
            c1[ord(char) - ord('a')] += 1
        
        for char in t:
            c2[ord(char) - ord('a')] += 1
        
        return c1 == c2


class TestIsAnagram:

    """
    pytest -s 242_valid_anagram.py::TestIsAnagram
    """

    def test(self):
        solution = Solution3()

        s = "anagram"; t = "nagaram"
        assert True == solution.isAnagram(s, t)

        s = "rat"; t = "car"
        assert False == solution.isAnagram(s, t)
