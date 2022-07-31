# -*- coding:utf-8 -*-


class Solution:

    """
    给你一个字符串 s, 由若干单词组成, 单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。
    单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
    """
    def lengthOfLastWord(self, s: str) -> int:
        sequence = s.split(" ")
        for word in sequence[::-1]:
            if word != "":
                break
        
        return len(word)


class TestLengthOfLastWord:

    """
    pytest -s 58_length_of_last_word.py::TestLengthOfLastWord
    """

    def test(self):

        solution = Solution()

        s = "Hello World"
        assert 5 == solution.lengthOfLastWord(s)

        s = "   fly me   to   the moon  "
        assert 4 == solution.lengthOfLastWord(s)

        s = "luffy is still joyboy"
        assert 6 == solution.lengthOfLastWord(s)
