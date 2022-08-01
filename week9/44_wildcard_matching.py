# -*- coding:utf-8 -*-


class Solution:

    """
    给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

    '?' 可以匹配任何单个字符。
    '*' 可以匹配任意字符串（包括空字符串）。

    两个字符串完全匹配才算匹配成功。
    说明:
        s 可能为空，且只包含从 a-z 的小写字母。
        p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
    """

    def isMatch(self, s: str, p: str) -> bool:
        pass


class TestIsMatch:

    """
    pytest -s 44_wildcard_matching.py::TestIsMatch
    """

    def test(self):
        solution = Solution()

        s = "aa"
        p = "a"
        assert False == solution.isMatch(s, p)

        s = "aa"
        p = "*"
        assert True == solution.isMatch(s, p)

        s = "cb"
        p = "?a"
        assert False == solution.isMatch(s, p)

        s = "adceb"
        p = "*a*b"
        assert True == solution.isMatch(s, p)

        s = "acdcb"
        p = "a*c?b"
        assert False == solution.isMatch(s, p)
