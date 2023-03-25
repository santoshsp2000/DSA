# 2316. Count Unreachable Pairs of Nodes in an Undirected Graph
from typing import List


class Solution:
    def dfs(self, node, adj, vis):
        vis[node] = 1
        count = 1
        for nod in adj[node]:
            if vis[nod] == 0:
                count += self.dfs(nod, adj, vis)

        return count

    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        vis = [0] * n
        ans = 0
        total = n

        for i in range(n):
            if vis[i] == 0:
                nodes = self.dfs(i, adj, vis)
                ans += nodes * (total - nodes)
                total -= nodes

        return ans
