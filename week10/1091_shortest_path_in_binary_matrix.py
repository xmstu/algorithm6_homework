# -*- coding:utf-8 -*-
from collections import deque, defaultdict
from typing import List


class Solution:
    """
    给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。

    二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n - 1)）的路径，该路径同时满足下述要求：
        - 路径途经的所有单元格都的值都是 0 。
        - 路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。
    畅通路径的长度 是该路径途经的单元格总数。
    """
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1:
            return -1
        if n == 1:
            return 1
        depth = defaultdict(int)
        start_point = (0, 0)
        q = deque()
        q.appendleft(start_point)
        depth[start_point] = 1

        visted = [[False] * n for _ in range(n)]
        visted[0][0] = True

        # 8 个方向, 上, 下, 左, 右, 右上, 左下, 右下, 左上 
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1), (1, 1), (-1, -1)]
        def isVaild(x, y):
            return 0 <= x < n and 0 <= y < n
        
        while q:
            x, y = q.pop()
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                if not isVaild(nx, ny) or grid[nx][ny] == 1 or visted[nx][ny]:
                    continue
                visted[nx][ny] = True
                depth[(nx, ny)] = depth[(x, y)] + 1
                if nx == n - 1 and ny == n - 1:
                    return depth[(nx, ny)]
                q.appendleft((nx, ny))
        
        return -1


class TestShortestPathBinaryMatrix:

    """
    pytest -s 1091_shortest_path_in_binary_matrix.py::TestShortestPathBinaryMatrix
    """

    def test(self):
        solution = Solution()

        grid = [
            [0,1],
            [1,0]
        ]
        assert 2 == solution.shortestPathBinaryMatrix(grid)

        grid = [
            [0,0,0],
            [1,1,0],
            [1,1,0]
        ]
        assert 4 == solution.shortestPathBinaryMatrix(grid)

        grid = [
            [1,0,0],
            [1,1,0],
            [1,1,0]
        ]
        assert -1 == solution.shortestPathBinaryMatrix(grid)
