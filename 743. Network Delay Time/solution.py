import collections
import heapq
from typing import List


class Solution:

    # Dijkstra algorithm, BFS + min Heap (priority queue)
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        edges = collections.defaultdict(list)

        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visit = set()
        t = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)  # weight, node
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t, w1)

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        return t if len(visit) == n else -1

        ## Time complexity: O(E*logV)

## Bellman-Ford algorithm: time complexity: O(VE)

## 其主要思想：对所有的边进行n-1轮松弛操作，因为在一个含有n个顶点的图中，任意两点之间的最短路径最多包含n-1边。
# 换句话说，第1轮在对所有的边进行松弛后，得到的是源点最多经过一条边到达其他顶点的最短距离；
# 第2轮在对所有的边进行松弛后，得到的是源点最多经过两条边到达其他顶点的最短距离；
# 第3轮在对所有的边进行松弛后，得到的是源点最多经过一条边到达其他顶点的最短距离

class Solution2(object):
    def networkDelayTime(self, times, n, k):
        dist = [float("inf")] * n
        dist[k - 1] = 0

        for _ in range(n - 1):
            for u, v, w in times:
                if (dist[u - 1] != float("Inf") and dist[v - 1] > w + dist[u - 1]):
                    dist[v - 1] = w + dist[u - 1]
        res = 0
        for i in range(n):
            if (dist[i] == float("inf")):
                return -1
            res = max(res, dist[i])
        return res


