# -*- coding:utf-8 -*-


class Solution:

    """
    给你一个字符串 jewels 代表石头中宝石的类型, 另有一个字符串 stones 代表你拥有的石头。 stones 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。
    字母区分大小写，因此 "a" 和 "A" 是不同类型的石头。
    """
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # 构建 jewels 的 set
        jewel_set = set()
        for jewel in jewels:
            jewel_set.add(jewel)
        
        jewel_num = 0
        for stone in stones:
            if stone in jewel_set:
                jewel_num += 1
        return jewel_num


class TestNumJewelsInStones:

    """
    pytest -s 771_jewels_and_stones.py::TestNumJewelsInStones
    """

    def test(self):
        solution = Solution()

        jewels = "aA"; stones = "aAAbbbb"
        assert 3 == solution.numJewelsInStones(jewels, stones)

        jewels = "z"; stones = "ZZ"
        assert 0 == solution.numJewelsInStones(jewels, stones)
