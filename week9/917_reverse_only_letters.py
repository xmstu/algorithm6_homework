# -*- coding:utf-8 -*-


class Solution:

    """
    给你一个字符串 s ，根据下述规则反转字符串：
    所有非英文字母保留在原有位置。
    所有英文字母（小写或大写）位置反转。
    返回反转后的 s 。
    """

    def reverseOnlyLetters(self, s: str) -> str:
        sequence = list(s)

        def is_english_letter(char: str) -> bool:
            return 'a' <= char <= 'z' or 'A' <= char <= 'Z'

        i, j = 0, len(s) - 1
        while i < j:
            if not is_english_letter(sequence[i]):
                i += 1
                continue
            if not is_english_letter(sequence[j]):
                j -= 1
                continue
            sequence[i], sequence[j] = sequence[j], sequence[i]
            i += 1
            j -= 1

        return "".join(sequence)


class TestReverseOnlyLetters:

    """
    pytest -s 917_reverse_only_letters.py::TestReverseOnlyLetters
    """

    def test(self):

        solution = Solution()

        s = "ab-cd"
        assert "dc-ba" == solution.reverseOnlyLetters(s)

        s = "a-bC-dEf-ghIj"
        assert "j-Ih-gfE-dCba" == solution.reverseOnlyLetters(s)

        s = "Test1ng-Leet=code-Q!"
        assert "Qedo1ct-eeLg=ntse-T!" == solution.reverseOnlyLetters(s)
