# -*- coding:utf-8 -*-


class Solution:

    """
    给定两个字符串 s 和 t, 判断它们是否是同构的。
    如果 s 中的字符可以按某种映射关系替换得到 t, 那么这两个字符串是同构的。
    每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。
    """

    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        思路: 用两个映射判断是否同构
        """
        s_map, t_map = {}, {}
        n = len(s)
        for index in range(n):
            s_map[s[index]] = t[index]
            t_map[t[index]] = s[index]
        
        # 判断是否同构
        for index in range(n):
            if s_map[s[index]] != t[index] or t_map[t[index]] != s[index]:
                return False

        return True


class TestIsIsomorphic:

    """
    pytest -s 205_isomorphic_strings.py::TestIsIsomorphic
    """

    def test(self):
        solution = Solution()

        s = "egg"; t = "add"
        assert True == solution.isIsomorphic(s, t)

        s = "foo"; t = "bar"
        assert False == solution.isIsomorphic(s, t)

        s = "paper"; t = "title"
        assert True == solution.isIsomorphic(s, t)

        s = "badc"; t = "baba"
        assert False == solution.isIsomorphic(s, t)
