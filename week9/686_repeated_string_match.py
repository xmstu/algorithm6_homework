# -*- coding:utf-8 -*-


from hashlib import new


class Solution:
    """
    给定两个字符串 a 和 b，寻找重复叠加字符串 a 的最小次数，使得字符串 b 成为叠加后的字符串 a 的子串，如果不存在则返回 -1。
    注意：字符串 "abc" 重复叠加 0 次是 ""，重复叠加 1 次是 "abc"，重复叠加 2 次是 "abcabc"。
    """
    def repeatedStringMatch(self, a: str, b: str) -> int:
        """
        思路: a 字符串叠加到刚好大于等于 b 串即可, 因为叠加的再多也没有意义
        b 属于 a 叠加子串的 共三种情况, 没有第四种情况, 再加 a 没有意义:
            1. b == k * a (叠加后的 a 字符串刚好和 b 长度一样, 并且完全匹配)
            2. b is substr (k * a + a) (叠加后的 a 字符串比 b 长, 但没有超出 len(a) 的长度, 此时 b 是 叠加 a 字符串 的 子串)
            3. b is substr (k * a + a + a) (叠加后的 a 字符串比 b 长, 并超出 len(a) 的长度, 此时 b 是 叠加 a 字符串 的 子串)
        """
        ans1 = ""
        k = len(b) // len(a)
        for _ in range(k):
            ans1 += a
        
        ans2 = ans1 + a
        ans3 = ans2 + a

        if b in ans1:
            return k
        elif b in ans2:
            return k + 1
        elif b in ans3:
            return k + 2
        else:
            return -1


class TestRepeatedStringMatch:

    """
    pytest -s 686_repeated_string_match.py::TestRepeatedStringMatch
    """

    def test(self):
        solution = Solution()

        a = "abcd"; b = "cdabcdab"
        assert 3 == solution.repeatedStringMatch(a, b)

        a = "a"; b = "aa"
        assert 2 == solution.repeatedStringMatch(a, b)

        a = "a"; b = "a"
        assert 1 == solution.repeatedStringMatch(a, b)

        a = "abc"; b = "wxyz"
        assert -1 == solution.repeatedStringMatch(a, b)

        a = "abc"; b = "cabcabca"
        assert 4 == solution.repeatedStringMatch(a, b)

