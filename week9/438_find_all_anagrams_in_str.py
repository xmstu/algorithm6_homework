# -*- coding:utf-8 -*-
from collections import defaultdict
from typing import List


class Solution:
    """
    给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
    异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
    """
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        思路: 每次判断是否异位词， 移动 step 步
        """
        p_len = len(p)
        s_len = len(s)
        p_map = defaultdict(int)
        for char in p:
            p_map[char] += 1

        def valid_anagrams(substr):
            step = 1
            substr_map = defaultdict(int)
            for index, char in enumerate(substr):
                if char not in p_map:
                    step = index + 1
                    continue
                substr_map[char] += 1
            is_valid = substr_map == p_map

            return is_valid, step


        ans = []
        i = 0
        while i + p_len <= s_len:
            # 判断 子串 是否 p 的 异位词
            substr = s[i:i+p_len]
            is_valid, step = valid_anagrams(substr)
            if is_valid:
                ans.append(i)
            i += step
        
        return ans


class Solution2:
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        维护p长度的滑动窗口进行比较

        根据题目要求，我们需要在字符串 s 寻找字符串 p 的异位词。
        因为字符串 p 的异位词的长度一定与字符串 p 的长度相同，
        所以我们可以在字符串 s 中构造一个长度为与字符串 p 的长度相同的滑动窗口，并在滑动中维护窗口中每种字母的数量；
        当窗口中每种字母的数量与字符串 p 中每种字母的数量相同时，则说明当前窗口为字符串 p 的异位词。
        """
        s_len, p_len = len(s), len(p)

        if s_len < p_len:
            return []
        
        ans = []
        s_count = [0] * 26
        p_count = [0] * 26

        # 计算第一段和 p 相同长度的 s 子串, 看是否为异位词
        for i in range(p_len):
            s_count[ord(s[i]) - ord("a")] += 1
            p_count[ord(s[i]) - ord("a")] += 1

        if s_count == p_count:
            ans.append(0)
        
        # 然后以 p_len 长度进行滑动
        for i in range(s_len - p_len):
            s_count[ord(s[i]) - ord('a')] -= 1
            s_count[ord(s[i + p_len]) - ord('a')] += 1

            if s_count == p_count:
                ans.append(i+1)
            
        return ans


class TestFindAnagrams:

    """
    pytest -s 438_find_all_anagrams_in_str.py::TestFindAnagrams
    """

    def test(self):
        solution = Solution2()

        s = "cbaebabacd"; p = "abc"
        assert [0,6] == solution.findAnagrams(s, p)

        s = "abab"; p = "ab"
        assert [0,1,2] == solution.findAnagrams(s, p)
