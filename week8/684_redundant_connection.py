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

    def connected(self, x, y):
        if self.find(x) == self.find(y):
            return True
        else:
            return False


class Solution:

    """
    思路:
        例子: edges = [[1,2], [1,3], [2,3]]
        利用并查集, 在每次遍历的时候划分分组,
        第一次遍历, edge: [1, 2], 1 归为 2 这个帮派
        第二次遍历, edge: [1, 3], 1 的父亲是 2, 2 和 3 组成更大的帮派, 此时, 2 的 父亲变为 3
        第三次遍历, edge: [2, 3], 2 的父亲是 3, 3 的父亲是自己, 已经连接了, 因此 [2, 3] 为冗余边
    """
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        disjointSet = DisjointSet(n+1)
        for i in range(n):
            # 提前判断是否相连, 
            if disjointSet.connected(edges[i][0], edges[i][1]):
                return edges[i]
            else:
                disjointSet.unionSet(edges[i][0], edges[i][1])
        
        return []


class TestFindRedundantConnection:

    """
    pytest -s 684_redundant_connection.py::TestFindRedundantConnection
    """

    def test(self):
        solution = Solution()

        edges = [[1,2], [1,3], [2,3]]
        assert [2,3] == solution.findRedundantConnection(edges)

        edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
        assert [1,4] == solution.findRedundantConnection(edges)

        edges = [[1,2],[2,3],[1,5],[3,4],[1,4]]
        assert [1,4] == solution.findRedundantConnection(edges)

        edges = [[1,5],[3,4],[3,5],[4,5],[2,4]]
        assert [4,5] == solution.findRedundantConnection(edges)
