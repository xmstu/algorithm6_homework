# -*- coding:utf-8 -*-
from typing import List


class DisjointSet:
	"""
	并查集

	find 将 x 和 x 的所有祖先连在根节点上, 因此树的高度只有2层
	unionSet 把两棵树进行合并, 只有当两个节点的最高层级的祖先不一致时, 才合并
	"""

	def __init__(self, n) -> None:
		self.fa = [i for i in range(n)]
	
	def find(self, x):
		if x == self.fa[x]:
			return x
		self.fa[x] = self.find(self.fa[x])
		return self.fa[x]
	
	def unionSet(self, x, y):
		x = self.find(x)
		y = self.find(y)
		if x != y:
			self.fa[x] = y


class Solution:

    """
    利用并查集获取岛屿数量, 将岛屿各自划分为一组, 最终扫描 fa 数组, 看有多少个自己的父亲是自己的, 就有多少个岛屿
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        disjointSet = DisjointSet(m * n)
        Dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False] * n for _ in range(m)]

        def in_area(x, y):
            return 0 <= x < m and 0 <= y < n
        
        def num(x, y):
            return x * n + y
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue
                for dx, dy in Dir:
                    ni, nj = i + dx, j + dy
                    if not in_area(ni, nj):
                        continue
                    if visited[ni][nj]:
                        continue
                    # 将所有在同一岛屿的归为一组
                    if grid[ni][nj] == "1":
                        disjointSet.unionSet(num(ni, nj), num(i, j))
                visited[i][j] = True
        
        ans = 0
        for i in range(m):
            for j in range(n):
                fa_index = num(i, j)
                if grid[i][j] == "1" and disjointSet.find(fa_index) == fa_index:
                    ans += 1
        
        return ans


class TestNumberOfIslands(object):
    """
    pytest -s 200_the_number_of_islands.py::TestNumberOfIslands
    """

    def test_solution(self):
        solution = Solution()
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        assert 1 == solution.numIslands(grid)

        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        assert 3 == solution.numIslands(grid)
