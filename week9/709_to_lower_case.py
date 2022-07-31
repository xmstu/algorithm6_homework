# -*- coding:utf-8 -*-


class Solution:
    """
    给你一个字符串 s ，将该字符串中的大写字母转换成相同的小写字母，返回新的字符串。
    """
    def toLowerCase(self, s: str) -> str:
        sequence = []
        for char in s:
            if "A" <= char <= "Z":
                new_char = chr(ord(char) - ord("A") + ord("a"))
                sequence.append(new_char) 
            else:
                sequence.append(char)

        return "".join(sequence)

class TestTolowerCase:

    """
    pytest -s 709_to_lower_case.py::TestTolowerCase
    """

    def test(self):
        solution = Solution()

        s = "Hello"
        assert "hello" == solution.toLowerCase(s)

        s = "here"
        assert "here" == solution.toLowerCase(s)

        s = "LOVELY"
        assert "lovely" == solution.toLowerCase(s)
