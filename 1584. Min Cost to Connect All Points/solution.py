import heapq
from typing import List


class Solution1:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        N = len(points)

        adj = {i: [] for i in range(N)}  # i: list of [cost, node]

        # create adjacent matrix
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Prim's algorithm
        res = 0
        visit = set()
        minH = [[0, 0]]  # [cost, point]
        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])

        return res

## Prim算法是以点为对象，挑选与点相连的最短边来构成最小生成树。
# 而Kruskal算法是以边为对象，不断地加入新的不构成环路的最短边来构成最小生成树。

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    # make a and b part of the same component
    # union by rank optimization
    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb: return
        if self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
            self.rank[pa] += self.rank[pb]
        else:
            self.parent[pa] = pb
            self.rank[pb] += self.rank[pa]

    # find the representative of the
    # path compression optimization
    def find(self, a):
        if self.parent[a] == a:
            return a

        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

## 并查集：https://www.zhihu.com/question/25257633/answer/2298724917

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))

        # sort based on cost (i.e. distance)
        edges.sort()

        # using Kruskal's algorithm to find the cost of Minimum Spanning Tree
        res = 0
        ds = DisjointSet(n)
        for cost, u, v in edges:
            if ds.find(u) != ds.find(v):
                ds.union(u, v)
                res += cost

        return res
