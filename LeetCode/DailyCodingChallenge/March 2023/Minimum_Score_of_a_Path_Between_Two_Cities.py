# 2492. Minimum Score of a Path Between Two Cities
from typing import List


class Solution:

    def minScore(self, n: int, roads: List[List[int]]) -> int:

        vis = [0] * (n + 1)
        adj = {i: [] for i in range(1, n + 1)}

        for row in roads:
            src, dist, wt = row[0], row[1], row[2]
            adj[src].append([dist, wt])
            adj[dist].append([src, wt])

        minn = [float('inf')]

        def dfs(node):
            vis[node] = 1
            for nod in adj[node]:
                minn[0] = min(minn[0], nod[1])
                if vis[nod[0]] == 0:
                    dfs(nod[0])

        dfs(1)
        return minn[0]
