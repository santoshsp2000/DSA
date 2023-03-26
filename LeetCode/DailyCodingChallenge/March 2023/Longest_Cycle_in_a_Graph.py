# 2360. Longest Cycle in a Graph
from typing import List


class Solution:
    def check(self, node, edges, vis):
        vis[node] = -1
        res = None
        if edges[node] == -1:
            pass
        elif vis[edges[node]] == 0:
            res = self.check(edges[node], edges, vis)
        elif vis[edges[node]] == -1:
            res = edges[node]
        vis[node] *= -1
        return res

    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        vis = [0] * n
        ans = 0

        for i in range(n):
            if vis[i] == 0:
                node = self.check(i, edges, vis)

                if node != None:
                    lenn = 1
                    start = node

                    while edges[node] != start:
                        lenn += 1
                        node = edges[node]
                    ans = max(ans, lenn)

        if ans == 0:
            return -1

        return ans
