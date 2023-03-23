# 1319. Number of Operations to Make Network Connected
from typing import List


class Solution:

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def dfs(node, adj, vis):
            vis[node] = 1
            for nod in adj[node]:
                if vis[nod] == 0:
                    dfs(nod, adj, vis)

        if n - 1 > len(connections): return -1

        adj = {i: [] for i in range(n)}

        for edge in connections:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        vis = [0] * n
        count = 0

        for i in range(n):
            if vis[i] == 0:
                count += 1
                dfs(i, adj, vis)

        return count - 1
